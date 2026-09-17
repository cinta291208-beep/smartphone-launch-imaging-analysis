---
name: smartphone-launch-imaging-analysis
description: Researches and produces evidence-based, visually polished smartphone launch and imaging analysis pages. Use for new-phone launch interpretation, camera-system analysis, multi-model comparisons, creator-review synthesis, third-party cross-checking, competitor implications, or an interactive HTML report for Apple, Xiaomi, OPPO, vivo, Samsung, Honor, Huawei and other phone brands.
---

# Smartphone Launch Imaging Analysis

Create a current, source-grounded analysis of a smartphone launch with special depth on imaging. The deliverable may be a research brief or a polished interactive HTML page. Adapt the framework to the product instead of forcing every phone into the same template.

## Use When

- A user asks to interpret a newly launched or upcoming smartphone, especially its camera system.
- A user wants official claims, specifications, creator reviews, third-party interpretations, and industry implications combined.
- Multiple models need to be compared without turning the page into a specification dump.
- A launch analysis should become a polished light-theme interactive webpage.
- A previous launch-day hands-on summary needs to be updated after full reviews are released.

## Don't Use When

- The user only wants a simple spec lookup; answer directly.
- The user asks only for shopping recommendations; use a shopping workflow.
- The device is old and the task is historical rather than launch/review analysis; use ordinary research unless this framework still adds value.
- Reliable primary or review sources do not yet exist; clearly label what is confirmed and what remains unavailable.

## Workflow

1. Establish scope and freshness.
   - Identify brand, models, launch date, region, current date, and whether full reviews are already available.
   - Treat launch-day hands-on content and later full reviews as different evidence classes.
2. Research primary sources first.
   - Search official product pages, newsroom/release posts, technical specifications, camera feature pages, and official launch material.
   - Extract official promotional wording when it is distinctive and useful.
   - Do not invent a cleaner slogan or feature name when the manufacturer already has one.
3. Build a normalized imaging fact sheet.
   - Record sensor/resolution, equivalent focal lengths, aperture, stabilization, zoom, macro, front camera, video formats/frame rates, log/RAW, audio, tracking, computational photography, and special form-factor features.
   - Separate physical optics, sensor/hardware, algorithms, controls, video workflow, audio, and interaction.
4. Compare models by role, not by raw table size.
   - Explain what each model is for and what imaging capabilities materially differ.
   - If there is one model, omit forced comparison sections.
   - If a foldable exists, include form factor as part of the imaging workflow.
5. Extract the official imaging story.
   - Preserve meaningful official phrases.
   - Cover all material official imaging features; do not omit less flashy video/audio features merely because they are below the fold.
   - Distinguish official claims from independent validation.
6. Research creators and independent reviewers.
   - Prefer the newest full review over launch-day hands-on content.
   - Search Bilibili, Weibo, YouTube, creator pages, reputable media summaries, and independent reviews as appropriate to the market.
   - For each creator capture: publication date, content type, tested model, main conclusion, imaging findings, non-imaging findings that affect purchase/use, caveats, and original link.
7. Cross-check creator claims.
   - Use reputable third-party reporting or independent tests to explain, corroborate, qualify, or challenge notable claims.
   - Never silently turn a third party's interpretation into the creator's own words.
   - Distinguish related technical phenomena precisely, e.g. ghosting versus flare, optical zoom versus optical-quality crop.
8. Synthesize after full reviews.
   - Explicitly explain what changed from launch-day attention to full-review conclusions.
   - Identify areas of multi-source agreement, disagreement, and still-unverified behavior.
   - Do not manufacture a consensus when sources test different conditions.
9. Derive industry implications.
   - Analyze optics, sensors, computational photography, video, audio, professional workflow, interaction, and competitor direction.
   - For Android/competitor discussion, compare concrete technical strategies rather than declaring a winner.
10. Design the page around information hierarchy.
   - Use a centered, restrained hero. Avoid unnecessary hero photography when typography and subtle gradients work better.
   - Avoid endless equal-sized card grids.
   - Use tabs or a left-side navigator for large feature families.
   - Make core selling points visually dominant; compress secondary features.
   - Add restrained hover/click micro-interactions and relevant icons/diagrams/images.
   - Keep source lists simple, vertical, numbered, and easy to audit.
11. Verify before delivery.
   - Check every important number against a source.
   - Check creator links and dates.
   - Check that current full reviews replaced stale hands-on summaries where appropriate.
   - Check responsive behavior, tab interactions, headings, overflow, and source visibility.
   - Remove meta-copy about how the page was researched or built.

## Rules

- Always search the web for current launch/review tasks. Freshness is part of correctness.
- Prefer primary manufacturer sources for official specifications and feature naming.
- Never describe a creator as having concluded something unless the source supports it.
- Clearly label third-party interpretations as third-party interpretations.
- Separate facts, manufacturer claims, reviewer observations, and synthesis.
- Do not treat a press release as independent evidence.
- Do not omit official video/audio features simply because camera hardware is more prominent.
- Do not write meta-copy such as “this page organizes”, “we verified”, “information was collected from”, or implementation commentary inside the final webpage.
- Avoid visual fatigue: do not render every fact as an equal card.
- Use progressive disclosure for dense content: tabs, side navigation, accordions, expandable evidence, or layered cards.
- Preserve whitespace and typographic hierarchy. Prefer a light, premium editorial style unless the user requests otherwise.
- Keep creator-review summaries comprehensive enough to include methodology/context, not just a one-sentence verdict.
- When a full review exists, demote launch-day hands-on content to supporting context.
- When sources disagree, explain test conditions and uncertainty instead of forcing one verdict.
- For competitor implications, discuss technical direction and tradeoffs, not brand cheerleading.
- Every external factual claim in a research answer should be traceable to a source.
- For the HTML artifact, include working source links and creator links, but keep the visible source section clean.
- If the page includes multiple product families, treat them as one launch story while still explaining their distinct imaging roles.
- Adapt section count to the device. Do not force a foldable section onto a slab phone or a telephoto section onto a device without one.

## Examples

- “解读小米下一代 Ultra 的影像升级，做成网页” → research official + creator + independent sources, emphasize sensor/telephoto/color/video, then generate the interactive report.
- “更新 vivo 新旗舰完整测评” → locate newer full reviews, replace stale launch-day hands-on summaries, add cross-source synthesis and what changed after testing.
- “对比 Galaxy Ultra 和 Pro Max 的影像方向” → compare documented optical, computational, video, workflow, and interaction strategies without declaring an overall winner.
- “分析一款新折叠屏手机” → add folding posture, external-screen preview, rear-camera selfie, multitasking/software adaptation, and durability/ergonomics evidence where available.

## Edge Cases

- Full reviews are embargoed: use official material + hands-on content, label the evidence stage, and avoid pretending long-term conclusions exist.
- Creator content is only discoverable through a search page: link the search result only as a fallback and avoid attributing details that were not verified.
- A third-party article paraphrases a creator: attribute the interpretation to the third party unless the original creator source confirms it.
- Regional specs differ: state the market/region and do not merge specifications silently.
- Marketing terms are ambiguous: quote or paraphrase the official term, then explain the underlying technical behavior separately.
- A claimed camera improvement depends on conditions: preserve those conditions, especially aperture, focal length, light direction, frame rate, stabilization mode, and software version.
- There are too many features for one viewport: use navigation/tabs and visual hierarchy rather than shrinking all cards equally.

## References

- See [references/research-method.md](references/research-method.md) for source priority, freshness, and verification.
- See [references/imaging-analysis-framework.md](references/imaging-analysis-framework.md) for the technical camera-analysis model.
- See [references/creator-review-framework.md](references/creator-review-framework.md) for creator and third-party synthesis.
- See [references/web-design-system.md](references/web-design-system.md) for the interactive webpage design language.
- See [references/page-structure.md](references/page-structure.md) for adaptive information architecture.
- Use [assets/report-template.html](assets/report-template.html) as a neutral starting shell when generating a standalone webpage.
- Run `scripts/validate_package.py` for basic package checks.
