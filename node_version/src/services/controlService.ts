
import GameController = require('gamecontroller');

export default class ControlService {
    type: string = '';
    constructor(type: string) {
        this.type = type;
    }

   conectControll(): void {
    const controller = new GameController(this.type);
   } 
};