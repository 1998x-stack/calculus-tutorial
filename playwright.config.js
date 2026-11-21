const { defineConfig } = require("@playwright/test");
module.exports = defineConfig({
 testDir:"./tests",timeout:30000,fullyParallel:true,reporter:"list",
 use:{baseURL:"http://127.0.0.1:4173",headless:true,trace:"retain-on-failure"},
 projects:[
  {name:"desktop",use:{viewport:{width:1440,height:900}}},
  {name:"tablet",use:{viewport:{width:768,height:1024}}},
  {name:"mobile-390",use:{viewport:{width:390,height:844}}},
  {name:"mobile-360",use:{viewport:{width:360,height:800}}}
 ],
 webServer:{command:"python3 -m http.server 4173 --bind 127.0.0.1",url:"http://127.0.0.1:4173",reuseExistingServer:!process.env.CI,timeout:10000}
});
