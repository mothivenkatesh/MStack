# Signzy MCC Classification & Onboarding Suite -- Competitive Intelligence (Step 2)

**Product:** Signzy's MCC Classification & Onboarding Suite (GST-to-MCC, WebCrawler, ShopLens AI, MSME Alt Data, Transaction Monitoring)
**ICP:** Merchant aggregators, PSPs, banks with merchant acquiring in India
**Date:** 2026-04-09

---

## 2. Competitive Intelligence

### Competitive Landscape

#### Direct Competitors

| Competitor | Their Positioning | Pricing Model | Strengths | Weaknesses | Our Angle |
|---|---|---|---|---|---|
| **Card91 (BlitzTrust / VerifyIQ)** | AI-powered merchant verification, dynamic MCC mapping, and risk scoring -- purpose-built for Indian card issuers and acquirers. Launched VerifyIQ (Apr 2026) as a full verification intelligence platform. | Usage-based API pricing (contact sales). Bundled with Card91's card infrastructure stack. | Deep India focus. Combines PAN/GSTIN/Udyam verification with AI-driven MCC assignment in one flow. RBI/NPCI/AML-compliant out of the box. Already embedded in card issuance workflows. | Primarily tied to Card91's card infrastructure customers -- not a standalone RegTech play. Limited to card-based acquiring; weaker in UPI/PA-Online merchant onboarding context. New product (VerifyIQ launched weeks ago), limited production track record. | Signzy is infrastructure-agnostic (works with any acquirer/PA, not locked to one card stack). 5-API suite goes beyond MCC assignment into ongoing transaction monitoring and MSME alt-data enrichment -- Card91 stops at onboarding. |
| **Parcha AI** | AI agents for merchant onboarding compliance. MCC classification from 500+ categories using business website + self-attested data analysis. US-headquartered, global focus. | Usage-based SaaS. Enterprise contracts (Flutterwave is a named customer). | 95-99.7% accuracy validated in production (Flutterwave case study). SOC 2 Type 2 compliant. Fast -- 2-5 min vs. 20-120 min manual. Strong API-first design. | US/global focus -- no India-specific data sources (GST, Udyam, MSME registries). Does not integrate with Indian identity rails (PAN, GSTIN, Aadhaar). No RBI-specific compliance framing. Limited presence in Indian BFSI ecosystem. | Signzy is built for India's regulatory fabric: GST-to-MCC mapping uses GSTIN as a primary signal (which Parcha cannot). ShopLens AI uses India-specific storefront intelligence. Deep integration with Indian identity and business verification rails. |
| **TrueBiz** | MCC Discovery -- assigns merchant category codes from just a business name + location using real-time web intelligence. Mastercard-approved MMSP. | Usage-based API. Enterprise tiers. Pricing not public. | Mastercard MMSP certification. Reduces application processing time by up to 80%. Works with minimal input (name + location). Plugs into risk engines and monitoring systems. | Western-market oriented. No India-specific data integrations (GST, Udyam, Shop & Establishment). Web-crawling approach works well for businesses with strong online presence but struggles with India's offline/MSME merchant base. No transaction monitoring component. | Signzy's ShopLens AI + MSME Alt Data APIs solve the India-specific "dark merchant" problem -- millions of MSMEs with minimal web presence. GST-to-MCC is a more authoritative signal than web crawling for Indian merchants. |
| **DeepVue.tech** | Merchant Category Classification API using computer vision / deep learning on retail storefront photographs. Also offers KYC/KYB APIs. | Per-API-call pricing. Self-serve + enterprise tiers. | Novel approach -- image-based MCC classification is useful for field verification. Has broader KYC/KYB API suite for Indian market. | Image-based classification requires field agents to capture storefront photos -- not scalable for digital-first onboarding. Limited to physical retail; cannot classify online-only or service businesses. No ongoing monitoring capability. Single-signal approach (image only). | Signzy's suite uses multiple signals (GST data, web crawl, storefront AI, MSME alt-data) rather than a single modality. Works for both physical and digital merchants. Covers full lifecycle from onboarding classification to ongoing transaction monitoring. |
| **Karza / Perfios (KGST Suite)** | GST verification and analytics APIs as part of a broader 100+ API KYC/KYB platform. GST stack live since 2017. Now part of Perfios (OneView). | Per-API-call. Volume-based enterprise pricing. Established in market. | Deepest GST data analytics in India (operational since 2017). Part of Perfios -- massive distribution through existing banking relationships. Trusted by major Indian banks and NBFCs. Comprehensive KYC/KYB coverage. | GST verification is a building block, not an MCC classification product. Compliance teams must still manually map GST data to MCC codes. No AI-driven MCC recommendation engine. No web crawling or storefront intelligence. No ongoing MCC drift monitoring. | Signzy automates the "last mile" that Karza leaves manual -- the GST-to-MCC mapping itself. Karza gives you the GST data; Signzy gives you the MCC decision. Positioning: "We start where Karza stops." |

#### Status Quo Competitor

**Manual MCC review + spreadsheet-based governance** remains the dominant approach for 70-80% of Indian merchant aggregators and PSPs today:

- **Process:** Compliance analyst receives merchant application with GST certificate. Manually looks up GSTIN on the GST portal. Reads the business description and HSN/SAC codes. Opens a Visa/Mastercard MCC reference PDF (500+ codes). Makes a judgment call on which MCC to assign. Enters it into the onboarding system. Periodic re-review (quarterly or annual) via spreadsheet audit.
- **Tools used:** GST portal (manual lookup), Excel/Google Sheets for MCC mapping tables, internal wikis with MCC guidelines, email-based escalation for edge cases.
- **Cost:** 15-30 minutes per merchant for initial classification. Error rates of 10-25% (industry estimates). Misclassification leads to interchange leakage, regulatory penalties (RBI PA Directions 2025 now mandate stricter MCC governance), and settlement disputes.
- **Why it persists:** "Good enough" for low volumes. Compliance teams are familiar with the process. No single product existed that combined GST-to-MCC automation with ongoing monitoring -- until now. Budget for tooling sits across compliance, risk, and ops -- hard to get a single PO signed.
- **Breaking point:** The RBI's September 2025 Master Direction on Payment Aggregators significantly raised the bar on merchant due diligence, MCC accuracy, and ongoing monitoring. Manual processes cannot scale with the new regulatory requirements, especially for PAs onboarding thousands of merchants monthly.

#### Adjacent Competitors

| Adjacent Competitor | What They Do | Overlap with Signzy MCC Suite | Gap |
|---|---|---|---|
| **AuthBridge** | India's largest RegTech -- digital KYC, video KYC, AML screening, workforce verification. 3,000+ enterprise clients, 15M+ monthly verifications. | Broad compliance and onboarding automation for BFSI. Could add MCC classification as a feature. | No MCC-specific product today. Focused on identity verification, not merchant categorization or transaction monitoring. |
| **IDfy** | AI/ML-driven KYC, KYB, digital onboarding. 600+ clients including HDFC, Axis, Paytm. 70M+ verifications. | Merchant onboarding verification (PAN, GST, business existence checks). | Identity-layer player. No MCC classification, no ongoing merchant category monitoring. |
| **HyperVerge** | AI-powered identity verification. 98% completion rate, 99% auto-approval. | Competes for "onboarding automation" budget. Some overlap in merchant KYC. | Pure identity verification. No business classification, no MCC mapping, no regulatory compliance workflow for PAs. |
| **LegitScript** | Mastercard-recognized MMSP. Merchant monitoring for high-risk categories across 100+ countries. 60+ risk detection areas. | Ongoing merchant monitoring and transaction compliance. Fine mitigation (75-100% BRAM/VIRP reduction). | Western-focused, content-risk oriented (pharmaceuticals, IP infringement). Not designed for India's MCC governance challenges. No GST integration. Premium pricing for global compliance, not tailored to Indian PA/PSP economics. |
| **Jocata (GRID platform)** | Unified AML, KYC remediation, fraud detection, case management for Indian banks/NBFCs. | Compliance workflow automation. Serves similar buyer (Head of Compliance). | Case management / AML platform, not MCC classification. Could be a complementary integration partner rather than competitor. |

---

### Market Maturity

**Phase: Early-to-Growing (Phase 1 transitioning to Phase 2 in FletchPMM's framework)**

Using FletchPMM's 3 Phases of Differentiation:

- **Phase 1 (Problem-Solution Fit / "Does it work?"):** The MCC classification automation market in India is still here for most buyers. The majority of merchant aggregators and PSPs are still doing MCC assignment manually. The problem is newly urgent (RBI PA Master Direction, September 2025), but most organizations have not yet purchased a dedicated tool. Buyers are evaluating whether automation is reliable enough to replace human judgment. Card91's VerifyIQ launched only in April 2026; Signzy's suite is new. The market is being created in real time.

- **Phase 2 signals (Feature-Function / "Does it do what I need?"):** A few early movers (Parcha, TrueBiz) exist globally, but the India-specific MCC classification market has fewer than 5 identifiable purpose-built products. Buyers who have adopted automation are now comparing features (accuracy, data sources, monitoring capabilities). RBI regulatory pressure is accelerating the move from Phase 1 to Phase 2.

**Differentiation mode for this phase:** Problem-aware education + proof of concept. The primary job is not to beat competitors on features but to convince the buyer that automated MCC classification is (a) necessary now (regulatory forcing function) and (b) reliable enough to trust (accuracy proof points, India-specific data advantage).

**Implication for positioning:** Lead with the problem (regulatory risk, manual process breakdown at scale) rather than features. Position Signzy as the category creator for "MCC Governance Automation" in India rather than a better version of something that already exists. Avoid premature feature comparison wars with global players (Parcha, TrueBiz) -- instead, frame the India-specific regulatory and data landscape as a moat they cannot cross.

---

### Top 3 Differentiation Angles

**1. India's Regulatory Fabric as a Moat (Data Advantage)**

No global competitor can replicate Signzy's integration with India's identity and business verification rails -- GSTIN, Udyam, Shop & Establishment, PAN, MCA. The GST-to-MCC API uses the most authoritative business classification signal available in India (HSN/SAC codes from GST filings) rather than web scraping or self-attestation. This is not a feature gap competitors can close with engineering effort; it requires deep regulatory domain expertise and government data source partnerships. Positioning line: "The only MCC engine built on India's regulatory data backbone."

**2. Full-Lifecycle Coverage (Onboarding + Monitoring, Not Just Classification)**

Every competitor stops at the point of MCC assignment during onboarding. Signzy's 5-API suite covers the full lifecycle: initial classification (GST-to-MCC, WebCrawler, ShopLens AI), enrichment for thin-file merchants (MSME Alt Data), and ongoing compliance (Transaction Monitoring for MCC drift detection). This matters because the RBI's 2025 PA Directions now require continuous merchant monitoring, not just point-in-time onboarding checks. Buyers purchasing a classification-only tool will need a second vendor for monitoring -- or they can get both from Signzy. Positioning line: "From Day 1 MCC assignment to Day 365 compliance -- one suite."

**3. The Dark Merchant Problem (MSME Alt-Data + ShopLens AI)**

India has 60M+ MSMEs, most with minimal or no web presence. Global MCC tools (Parcha, TrueBiz) that rely on web crawling and online business intelligence are structurally unable to classify these merchants. Signzy's ShopLens AI (storefront/physical presence analysis) combined with MSME Alt Data (alternative business signals beyond GST and web) solves the classification challenge for India's long tail of offline and semi-formal merchants. This is the segment where acquirers and PAs face the highest misclassification risk and regulatory exposure. Positioning line: "Classify the merchants no one else can see."

---

### Sources

- [Parcha AI - MCC Classification](https://www.parcha.ai/agents/mcc-classification)
- [TrueBiz - MCC Discovery](https://truebiz.io/blog/mcc-discovery)
- [Card91 - AI-Powered Merchant Verification & MCC Mapping](https://card91.io/ai-lab/merchant-verification-classification)
- [DeepVue - Merchant Category Verification](https://deepvue.tech/retailer-tech/merchant-category-verification/)
- [Karza / Perfios - GST & Onboarding](https://karza.in/products/Gst)
- [AuthBridge - 7 Best RegTech Platforms in India](https://authbridge.com/blog/7-best-regtech-platforms-in-india/)
- [HyperVerge - Signzy Competitors](https://hyperverge.co/blog/signzy-competitors/)
- [LegitScript - MMSP](https://www.legitscript.com/mmsp/)
- [RBI PA Master Direction 2025](https://www.fidcindia.org.in/wp-content/uploads/2025/09/RBI-PAYMENT-AGGREGATORS-DIRECTIONS-15-09-25.pdf)
- [India RegTech Market - IMARC Group](https://www.imarcgroup.com/india-regtech-market)
- [Signzy Platform](https://www.signzy.com/)
- [Card91 VerifyIQ Launch](https://www.prnewswire.com/in/news-releases/card91-launches-ai-powered-merchant-verification-and-classification-suite-to-simplify-and-secure-onboarding-302514721.html)
