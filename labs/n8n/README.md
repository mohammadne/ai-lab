# N8N

due to `ngrok` limitations, I run this server outside Iran.

```sh
docker compose up -d
```

```sh
wget https://bin.ngrok.com/c/bNyj1mQVY4c/ngrok-v3-stable-linux-amd64.tgz
sudo tar -xvzf ~/Downloads/ngrok-v3-stable-linux-amd64.tgz -C /usr/local/bin
ngrok config add-authtoken 3GFkbJQ1sOe1x2qrW9CE8Z6JTZY_6dN3J18ZySp6vbhUEkziv
ngrok http --url=popcorn-cradle-vanilla.ngrok-free.dev 5678
```

```sh
ssh -N -R 127.0.0.1:5678:localhost:5678 gozar-server
```
