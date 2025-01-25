// Pick

interface User {
    id: number;
    name:string;
    email:string;
    createdAt: Date;
}

type UserProfile = Pick<User,'name' | 'email'>;

const displayProfile = (user: UserProfile) => {
    console.log(user.email)
}

const usr: UserProfile = {
    name: "sheninthjr",
    email: "sh@gmail.com",
}
displayProfile(usr)

// ReadOnly

interface Config {
    readonly endpoint: string;
    readonly apikey:string;
}

const config: Readonly<Config> = {
    endpoint: "https://sheninthjr.com",
    apikey: "helo"
}

// Exclude

type event = 'click' | 'scroll' | 'mousemove';
type ExcludeEvent = Exclude<event,"scroll">;

const handleEvent = (event: ExcludeEvent) => {
    console.log(event);
}

handleEvent("click")

type partial = Partial<UserProfile>;

const username: partial = {
    name: "sheninthjr"
}