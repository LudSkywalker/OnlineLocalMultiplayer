const express = require("express");
const app = express();
const http = require("http");
const server = http.createServer(app);
const { Server } = require("socket.io");
const io = new Server(server);

app.get("/", (req, res) => {
	res.sendFile(__dirname + "/index.html");
});

io.on("connection", (socket) => {
	console.log("a user connected");
	socket.on("key", (key) => {
        console.log(key);
		io.emit("key",key);
	});
});

server.listen(process.env.PORT?process.env.PORT:3000, () => {
	console.log(`listening on port:${process.env.PORT?process.env.PORT:
    3000}`);
});