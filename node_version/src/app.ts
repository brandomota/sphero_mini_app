import { Scanner, Utils } from 'spherov2.js';
//const control = 



const initApp = async () => {
    try{
        const sphero =  await Scanner.findSpheroMini();
        sphero.wake();
    } catch(e) {
        console.log(e);
    }

}

initApp();