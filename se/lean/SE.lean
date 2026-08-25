-- Root module for the node-linked Set Equality development.
-- Support (non-node) modules
import SE.Support.Defs
import SE.Support.Cbrt
import SE.Support.Constants
import SE.Support.Envelope
import SE.Support.Limits
-- Tier-2 support: the explicit hook product, the hook ratio `p₀`/`ω`, the telescoping identities,
-- the BR/Φ branch constants, and what they prove
import SE.Support.Telescope
import SE.Support.Hook
import SE.Support.Omega
import SE.Support.BranchFactors
-- The cited interface (non-node)
import SE.Interface
import SE.Support.RhoEnvelope
-- Node modules (import order = topological order of the DAG)
import SE.denom.Phi.legal.trace.t6
import SE.denom.Phi.legal.gram.interface
import SE.denom.Phi.legal.omega.interface
import SE.denom.Phi.legal.sect
import SE.denom.Phi.legal.tame
import SE.denom.taper
import SE.denom
import SE.br
import SE.goal
-- Self-tests and the trust boundary (non-node)
import SE.SelfTest
import SE.Trust
