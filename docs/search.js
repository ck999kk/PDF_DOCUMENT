async function load(u){
  try{
    const r=await fetch(u);
    const t=await r.text();
    return t.split("\n").filter(Boolean).map(JSON.parse);
  }catch(e){
    console.error("Failed to load index",e);
    const res=document.getElementById("res");
    if(res)res.textContent="Failed to load index";
    return[];
  }
}
function hit(r,q){q=q.toLowerCase();return r.text.toLowerCase().includes(q)}
const esc=s=>s.replace(/[&<>]/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;'}[c]));
(async()=>{
  const data=await load("../index.jsonl");
  const q=document.getElementById("q"),res=document.getElementById("res");
  function render(list){
    res.innerHTML=list.slice(0,200).map(r=>`<div><a href="${r.url}" target="_blank">${r.file}</a> — p.${r.page}<br>${esc(r.text)}</div><hr>`).join("")
  }
  q.addEventListener("input",()=>{const v=q.value.trim(); if(!v){res.innerHTML=""; return} render(data.filter(r=>hit(r,v)));});
})();
