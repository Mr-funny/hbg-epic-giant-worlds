# Prompt contract

## Mother-image prompt

Write in complete visual sentences and include:

```text
Use case and exact 16:9 asset type
Keyword and one-sentence visual thesis
Credible world and spatial setting
Foreground family and exact anchor
Midground human stage
Tiny people and one quiet action
Atmospheric expanse
One keyword-derived megastructure
At most one cosmic anchor with negative space
Camera relationship, lens, horizon, subject placement, leading line
Natural light, atmosphere, palette, materials, regional ornament
Cultural constraints
Negative constraints
```

Do not demand every object be centered or symmetric. Do not use a tree unless it is culturally or ecologically justified.

## Image-relative Veo/Gemini prompt

```text
Create one continuous 8-second cinematic image-to-video shot from the provided initial frame.

Preserve exactly: [visible foreground], [midground stage], [people and positions], [atmosphere], [giant structure], [celestial anchor], [light direction], [palette].

Camera: start from the exact composition; perform one slow stabilized [path]; end moderately changed while retaining an ultra-wide establishing view. No cut, snap zoom, orbit, shake, or acceleration.

Parallax: [foreground] moves most, [midground] moderately, [distant giant form/celestial body] almost not at all.

Environment: [three to five physically supported motions]. People perform [one minimal action].

Rigid constraints: no redesign, bending, melting, growth, duplication, new landmark, new crowd, false writing, enlarged people, energy beam, scene transition, timelapse, weather replacement, logo, or watermark.

Audio: only natural sounds supported by the visible environment, unless requested otherwise.
```

The motion prompt must name visible facts. If no image exists, call it a motion plan rather than an image-relative prompt.

