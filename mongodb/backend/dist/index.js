"use strict";
var __awaiter = (this && this.__awaiter) || function (thisArg, _arguments, P, generator) {
    function adopt(value) { return value instanceof P ? value : new P(function (resolve) { resolve(value); }); }
    return new (P || (P = Promise))(function (resolve, reject) {
        function fulfilled(value) { try { step(generator.next(value)); } catch (e) { reject(e); } }
        function rejected(value) { try { step(generator["throw"](value)); } catch (e) { reject(e); } }
        function step(result) { result.done ? resolve(result.value) : adopt(result.value).then(fulfilled, rejected); }
        step((generator = generator.apply(thisArg, _arguments || [])).next());
    });
};
var __importDefault = (this && this.__importDefault) || function (mod) {
    return (mod && mod.__esModule) ? mod : { "default": mod };
};
Object.defineProperty(exports, "__esModule", { value: true });
const mongoose_1 = __importDefault(require("mongoose"));
const mongodb_1 = require("mongodb");
const db_1 = require("./db");
mongoose_1.default.connect('mongodb://localhost:27017/test').then(() => {
    console.log("Db connected");
});
function main() {
    return __awaiter(this, void 0, void 0, function* () {
        const id = new mongodb_1.ObjectId();
        const data = new db_1.User({ id: id, title: "Want to get successfull" });
        yield data.save();
        const userDetails = yield db_1.User.find();
        console.log(userDetails);
    });
}
main();
