// Cacao design system: motion.
// 1. Lenis smooth scroll (assets/vendor/lenis.min.js), also for in-page anchor links.
// 2. Vanta fog behind any element with data-vanta="fog", on wide screens only.
//    three.js + Vanta are loaded only when needed. Colours and speed come from tokens.css.
// Both are skipped when the visitor prefers reduced motion.
(function(){
  var reduce = matchMedia('(prefers-reduced-motion: reduce)').matches;
  var css = getComputedStyle(document.documentElement);
  function token(name){ return css.getPropertyValue(name).trim(); }
  function hex(name){ return parseInt(token(name).replace('#',''),16); }
  function num(name){ return parseFloat(token(name)); }
  var base = (document.currentScript && document.currentScript.src || '').replace(/motion\.js.*$/, '');

  function load(src){ return new Promise(function(ok, fail){ var s=document.createElement('script'); s.src=base+src; s.onload=ok; s.onerror=fail; document.head.appendChild(s); }); }

  // Lenis
  if (!reduce && window.Lenis) {
    var nav = document.querySelector('.nav');
    var lenis = new Lenis({ duration: num('--scroll-duration') || 1.2, anchors: { offset: nav ? -nav.offsetHeight : 0 } });
    function raf(t){ lenis.raf(t); requestAnimationFrame(raf); }
    requestAnimationFrame(raf);
    window.cacaoLenis = lenis;
  }

  // Vanta fog
  var targets = [].slice.call(document.querySelectorAll('[data-vanta="fog"]'));
  if (reduce || !targets.length || window.innerWidth < (num('--vanta-min-width') || 821)) return;
  load('vendor/three.min.js').then(function(){ return load('vendor/vanta.fog.min.js'); }).then(function(){
    targets.forEach(function(el){
      try {
        VANTA.FOG({ el: el, THREE: window.THREE, mouseControls: true, touchControls: false, gyroControls: false,
          highlightColor: hex('--vanta-highlight'), midtoneColor: hex('--vanta-midtone'),
          lowlightColor: hex('--vanta-lowlight'), baseColor: hex('--vanta-base'),
          blurFactor: num('--vanta-blur'), speed: num('--vanta-speed'), zoom: num('--vanta-zoom') });
      } catch (e) { /* no WebGL: the hero keeps its plain background */ }
    });
  }).catch(function(){});
})();
