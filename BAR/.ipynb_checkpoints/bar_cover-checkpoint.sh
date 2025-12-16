#!/bin/bash
# ~/bin/bar_cover.sh
# chmod +x ~/bin/bar_cover.sh
# deps: feh, imagemagick (convert)

PIDFILE=/tmp/screen_patches.pid
COLOR=${PATCH_COLOR:-black}   # set PATCH_COLOR env to override (e.g., "red" or "rgba(0,0,0,0.6)")


# Rectangles in WxH+X+Y form (from xrectsel)
RECTS=(
  "205x100+336+26"
  "335x200+272+190"
  "335x190+272+420"
  "563x252+210+720"
  "248x274+828+720"
  # "100x10+545+65"
  # "10x100+545+65"
)

# --- TOGGLE LOGIC ---
if [ -f "$PIDFILE" ]; then
  echo "Killing existing patches..."
  while read -r pid; do
    kill "$pid" 2>/dev/null
  done < "$PIDFILE"
  rm -f "$PIDFILE"
  exit 0
fi

# --- CREATE PATCHES ---
rm -f "$PIDFILE"
i=0
for spec in "${RECTS[@]}"; do
  i=$((i+1))

  IFS='x+' read -r W H X Y <<< "$spec"

  IMG="/tmp/patch_${i}_${W}x${H}.png"
  # Solid opaque color. For semi-transparent, use canvas:rgba(0,0,0,0.6)
  convert -size "${W}x${H}" "xc:${COLOR}" "$IMG"

  feh --geometry "${W}x${H}+${X}+${Y}" --borderless --no-fehbg "$IMG" &
  echo $! >> "$PIDFILE"
done
