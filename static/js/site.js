document.addEventListener('DOMContentLoaded',()=>{
  const toggle=document.querySelector('.menu-toggle'),menu=document.querySelector('#mobile-menu'),close=document.querySelector('.menu-close');
  const setMenu=open=>{if(!menu)return;menu.hidden=!open;toggle?.setAttribute('aria-expanded',String(open));document.body.style.overflow=open?'hidden':''};
  toggle?.addEventListener('click',()=>setMenu(true));close?.addEventListener('click',()=>setMenu(false));menu?.querySelectorAll('a').forEach(a=>a.addEventListener('click',()=>setMenu(false)));
  const buttons=document.querySelectorAll('[data-filter]'),cards=document.querySelectorAll('[data-position]'),empty=document.querySelector('#empty-players');
  buttons.forEach(button=>button.addEventListener('click',()=>{buttons.forEach(b=>b.classList.remove('active'));button.classList.add('active');let count=0;cards.forEach(card=>{const show=button.dataset.filter==='all'||card.dataset.position===button.dataset.filter;card.hidden=!show;if(show)count++});if(empty)empty.hidden=count!==0;}));
});
