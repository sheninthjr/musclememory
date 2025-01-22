import { model, Schema } from "mongoose";


const userSchema = new Schema({
    id: Schema.ObjectId,
    title: String
})

export const User = model('User',userSchema)