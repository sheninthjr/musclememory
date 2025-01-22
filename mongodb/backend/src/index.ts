import mongoose from "mongoose";
import { ObjectId } from "mongodb";
import { User } from "./db";

mongoose.connect('mongodb://localhost:27017/test').then(() => {
    console.log("Db connected")
})

async function main() {
    const id = new ObjectId();
    const data = new User({id: id, title: "Want to get successfull"});
    await data.save();
    const userDetails = await User.find();
    console.log(userDetails)
}
main();