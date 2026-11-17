(function (root) {
  "use strict";

  function boxAt(point, width, height) {
    return {x1: point.x - width / 2, y1: point.y - height / 2,
      x2: point.x + width / 2, y2: point.y + height / 2};
  }

  function overlaps(a, b, gap = 0) {
    return a.x1 < b.x2 + gap && a.x2 > b.x1 - gap &&
      a.y1 < b.y2 + gap && a.y2 > b.y1 - gap;
  }

  function bendThrough(source, target, point) {
    const dx = target.x - source.x;
    const dy = target.y - source.y;
    const squaredLength = dx * dx + dy * dy;
    if (squaredLength < 1) return null;
    return {
      weight: ((point.x - source.x) * dx + (point.y - source.y) * dy) / squaredLength,
      distance: (dx * (point.y - source.y) - dy * (point.x - source.x)) / Math.sqrt(squaredLength)
    };
  }

  function segmentCrossesBox(start, end, box) {
    const dx = end.x - start.x, dy = end.y - start.y;
    const p = [-dx, dx, -dy, dy];
    const q = [start.x - box.x1, box.x2 - start.x, start.y - box.y1, box.y2 - start.y];
    let first = 0, last = 1;
    for (let i = 0; i < 4; i++) {
      if (Math.abs(p[i]) < 1e-9) {
        if (q[i] < 0) return false;
      } else {
        const t = q[i] / p[i];
        if (p[i] < 0) first = Math.max(first, t);
        else last = Math.min(last, t);
        if (first > last) return false;
      }
    }
    return true;
  }

  function contains(box, point) {
    return point.x >= box.x1 && point.x <= box.x2 && point.y >= box.y1 && point.y <= box.y2;
  }

  function placeLabels(labels, obstacles, gap = 8) {
    const occupied = obstacles.slice();
    const placements = new Map();
    // Reserve large labels first, with stable ordering for parallel edges.
    const ordered = labels.slice().sort((a, b) =>
      b.width * b.height - a.width * a.height || a.id.localeCompare(b.id));
    ordered.forEach(label => {
      const dx = label.target.x - label.source.x;
      const dy = label.target.y - label.source.y;
      const length = Math.hypot(dx, dy) || 1;
      const normal = {x: -dy / length, y: dx / length};
      if (!dx && !dy) normal.y = 1;
      const anchors = [label.origin, ...[.5, .35, .65, .22, .78].map(weight => ({
        x: label.source.x + dx * weight, y: label.source.y + dy * weight
      }))];
      const candidates = [];
      for (const distance of [0, 16, 32, 56, 88, 128, 184, 256]) {
        for (const direction of distance ? [1, -1] : [1]) {
          for (const anchor of anchors) {
            const point = {x: anchor.x + normal.x * distance * direction,
              y: anchor.y + normal.y * distance * direction};
            candidates.push({...point,
              score: Math.hypot(point.x - label.origin.x, point.y - label.origin.y) + distance * .35});
          }
        }
      }
      const free = candidates.filter(candidate => {
        const box = boxAt(candidate, label.width, label.height);
        return occupied.every(obstacle => !overlaps(box, obstacle, gap));
      });
      free.forEach(candidate => {
        const crossings = occupied.filter(box => !contains(box, label.source) && !contains(box, label.target) &&
          (segmentCrossesBox(label.source, candidate, box) || segmentCrossesBox(candidate, label.target, box))).length;
        candidate.score += crossings * 1200;
      });
      free.sort((a, b) => a.score - b.score);
      let point = free[0];
      // Even crowded or self-loop cases get a free label, never a hidden one.
      if (!point) point = {
        x: label.origin.x,
        y: Math.min(label.origin.y, ...occupied.map(box => box.y1)) - label.height / 2 - gap - 1
      };
      const box = boxAt(point, label.width, label.height);
      occupied.push(box);
      placements.set(label.id, {x: point.x, y: point.y, box});
    });
    return placements;
  }

  const api = {placeLabels, bendThrough, overlaps, segmentCrossesBox};
  if (typeof module === "object" && module.exports) module.exports = api;
  else root.OntolensGraphLabels = api;
})(typeof globalThis === "undefined" ? this : globalThis);
