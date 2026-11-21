const {chromium}=require('playwright');
(async()=>{const b=await chromium.launch();const p=await b.newPage({viewport:{width:1080,height:1350}});
for(const s of ['PNJ','FPT']){await p.goto('file://'+process.cwd()+'/'+s+'.html');await p.waitForFunction(()=>document.title==='xong');await p.screenshot({path:s+'_lo.jpg',type:'jpeg',quality:92});}
await b.close();})();
