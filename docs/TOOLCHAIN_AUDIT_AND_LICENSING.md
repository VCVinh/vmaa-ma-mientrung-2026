# Toolchain Technical Architecture, Data-Flow Audit & Licensing Assessment
**Project:** VMAA M&A Miền Trung 2026 — International Motion Identity System  
**Audit Date:** October 2026  
**Auditor:** Integrated Creative Studio & Production Architecture Swarm

---

## 1. OpenHiggsfield (`wide-trace/open-higgsfield`)
- **Repository Assessment:** OpenHiggsfield provides an experimental unified studio interface aggregating multiple video generation APIs via a single prompt bar.
- **Data Flow & Privacy Risk:**
  - The architecture requires external cloud platform API keys (Runway, Luma, Kling, etc.).
  - Default asset pipeline uploads generated videos and prompt assets to **Vercel Blob** cloud storage.
  - **Client Confidentiality Verdict:** Client assets (official corporate vector logos, executive portraits, proprietary financial deal deck numbers) **must NOT** be piped through unverified third-party cloud storage or public blob storage.
  - **Production Recommendation:** For production-grade brand identities, use local node-based **ComfyUI** with open-weights models (Wan 2.2 / LTX-2.5) on isolated local hardware for raw visual plates, and execute **100% deterministic code** (HTML5 Canvas, Playwright, GSAP, CSS3) for all typography, logos, and lower-third animations.

---

## 2. GSAP & ScrollTrigger (`greensock/GSAP`)
- **License Status:** Webflow officially acquired GreenSock and updated GSAP licensing to **Standard Permissive Commercial Use** (free for commercial and client production websites).
- **Production Capability:**
  - Unmatched deterministic precision for masked reveals, SVG path morphs, timeline synchronization, and pinned scroll sections.
  - Flawless hardware-accelerated transforms (`translate3d`, `opacity`, `clip-path`) avoiding layout recalculations.
- **Role in VMAA 2026:** Serves as the primary motion orchestration engine for the landing page and the guest invitation lower-third reveal sequence.

---

## 3. Three.js & React Three Fiber (`pmndrs/react-three-fiber`)
- **License Status:** MIT License (100% open source and commercially unrestricted).
- **Architectural Policy:**
  - Restricted strictly to the Hero and the signature "Architecture of Value" visual.
  - Avoids bloated full-page 3D canvas rendering that would degrade battery life or cause mobile overheating.
  - Includes explicit WebGL context destruction (`geometry.dispose()`, `material.dispose()`) and automatic fallback to CSS3 layered planes when WebGL is unsupported or when `prefers-reduced-motion` is active.

---

## 4. Motion Primitives & Magic UI (`ibelick/motion-primitives` · `magicuidesign/magicui`)
- **License Status:** MIT License.
- **Art Direction Discipline:** Selected sparingly for subtle border-beam scans, glass reflections, and micro-interactions. No random stacking of disparate components; all styling enforces the VMAA Obsidian-Cobalt Design Bible.

---

## 5. Lenis Smooth Scroll (`darkroomengineering/lenis`)
- **License Status:** MIT License.
- **Accessibility & UX Guardrails:**
  - Integrated with smooth scrolling disabled whenever `prefers-reduced-motion: reduce` is detected.
  - Touch devices receive native touch momentum scrolling to prevent input lag.
  - Keyboard focus and navigation (`Tab`, `Space`, `PageUp`, `PageDown`) remain standard and unimpeded.
