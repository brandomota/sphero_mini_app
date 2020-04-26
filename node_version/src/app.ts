const { Scanner, Utils } = require('spherov2.js');
//const control = 



const initApp = async () => {
    try{
        const sphero =  await Scanner.findAll();
        sphero.wake();
    } catch(e) {
        console.log(e);
    }

}

initApp();