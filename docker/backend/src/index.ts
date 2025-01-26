import 'dotenv/config'
import express, { Response, Request } from 'express'
import cors from 'cors'

const app = express()
app.use(express.json())
app.use(cors())

console.log(process.env.DATABASE_URL)

app.get('/',(req:Request,res: Response) => {
    const body = req.body.username;
    res.send("Hi from the backend")
})

app.listen(3003,() => {
    console.log("Server is up")
})