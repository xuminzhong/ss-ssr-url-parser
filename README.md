# ss-ssr-url-parser

> ss、ssr url parser, which can decode ss\ssr url

## Environment

- python3+

## How To Use

### Just Test:

```
python ss_ssr_decode
```

### Import To Your Code

```
form ss_ssr_decode import parse

result = parse('your ss/ssr url here')
print(result)
```

## Result Format

### ss

```
{'method': 'aes-128-ctr', 'password': 'viencoding.com', 'ip': '152.89.208.146', 'port': '2333'}
```

### ssr

```
{'ip': '152.89.208.146', 'port': '2333', 'protocol': 'auth_sha1_v4', 'method': 'aes-128-ctr', 'obfs': 'plain', 'password': 'viencoding.com'}
{'ip': 'xxx.com', 'port': '8080', 'protocol': 'origin', 'method': 'AES-128-CFB', 'obfs': 'http_post', 'password': '123456', 'obfsparam': 'xxx.qq.com', 'protoparam': 'abcd:defg==', 'remarks': 'hk', 'group': 'ssr-vpn'}
```

## End

That's all. Hope you have a fun to use.

## Other

### Online QRCode Generator For ss/ssr

[ss-ssr-qrcode-generator](https://viencoding.com/ss-ssr-qrcode-generator)
