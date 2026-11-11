import Foundation
import PDFKit
import CoreGraphics
import ImageIO
import UniformTypeIdentifiers

let args = CommandLine.arguments
guard args.count >= 3 else { print("usage: pdftool <pdf> <cmd:text|find|render> [args]"); exit(1) }
let url = URL(fileURLWithPath: args[1])
guard let doc = PDFDocument(url: url) else { print("cannot open"); exit(1) }
let cmd = args[2]

if cmd == "npages" { print(doc.pageCount) }

if cmd == "text" {
    let p = Int(args[3])!
    if let pg = doc.page(at: p-1) { print("=== page \(p) ==="); print(pg.string ?? "") }
}

if cmd == "find" {
    let needle = args[3]
    for i in 0..<doc.pageCount {
        if let s = doc.page(at: i)?.string, s.contains(needle) {
            print("page \(i+1) contains \(needle)")
        }
    }
}

if cmd == "render" {
    let p = Int(args[3])!
    let dpi = Double(args[4])!
    let out = args[5]
    guard let pg = doc.page(at: p-1) else { print("no page"); exit(1) }
    let box = pg.bounds(for: .mediaBox)
    let scale = dpi / 72.0
    let w = Int((box.width * scale).rounded())
    let h = Int((box.height * scale).rounded())
    let cs = CGColorSpaceCreateDeviceRGB()
    guard let ctx = CGContext(data: nil, width: w, height: h, bitsPerComponent: 8,
                              bytesPerRow: 0, space: cs,
                              bitmapInfo: CGImageAlphaInfo.premultipliedLast.rawValue) else { exit(1) }
    ctx.setFillColor(CGColor(red:1,green:1,blue:1,alpha:1))
    ctx.fill(CGRect(x:0,y:0,width:w,height:h))
    ctx.saveGState()
    ctx.scaleBy(x: scale, y: scale)
    ctx.translateBy(x: -box.origin.x, y: -box.origin.y)
    ctx.setAllowsAntialiasing(true)
    ctx.interpolationQuality = .high
    pg.draw(with: .mediaBox, to: ctx)
    ctx.restoreGState()
    guard let img = ctx.makeImage() else { exit(1) }
    let ourl = URL(fileURLWithPath: out) as CFURL
    guard let dest = CGImageDestinationCreateWithURL(ourl, UTType.png.identifier as CFString, 1, nil) else { exit(1) }
    CGImageDestinationAddImage(dest, img, nil)
    CGImageDestinationFinalize(dest)
    print("wrote \(out) \(w)x\(h) at \(dpi) dpi (mediaBox \(box))")
}

if cmd == "crop" {
    // crop <page> <dpi> <x0> <y0> <x1> <y1> <out>   -- coords in PDF points, origin bottom-left
    let p = Int(args[3])!, dpi = Double(args[4])!
    let x0 = Double(args[5])!, y0 = Double(args[6])!, x1 = Double(args[7])!, y1 = Double(args[8])!
    let out = args[9]
    guard let pg = doc.page(at: p-1) else { exit(1) }
    let scale = dpi/72.0
    let w = Int(((x1-x0)*scale).rounded()), h = Int(((y1-y0)*scale).rounded())
    let cs = CGColorSpaceCreateDeviceRGB()
    guard let ctx = CGContext(data: nil, width: w, height: h, bitsPerComponent: 8, bytesPerRow: 0,
                              space: cs, bitmapInfo: CGImageAlphaInfo.premultipliedLast.rawValue) else { exit(1) }
    ctx.setFillColor(CGColor(red:1,green:1,blue:1,alpha:1)); ctx.fill(CGRect(x:0,y:0,width:w,height:h))
    ctx.scaleBy(x: scale, y: scale)
    ctx.translateBy(x: -x0, y: -y0)
    pg.draw(with: .mediaBox, to: ctx)
    guard let img = ctx.makeImage() else { exit(1) }
    guard let dest = CGImageDestinationCreateWithURL(URL(fileURLWithPath: out) as CFURL, UTType.png.identifier as CFString, 1, nil) else { exit(1) }
    CGImageDestinationAddImage(dest, img, nil); CGImageDestinationFinalize(dest)
    print("wrote \(out) \(w)x\(h)")
}
