import binascii
import base64


crypto_js = open('crypto.js').read()
hotp_js = open('hotp.js').read()
myotp_js = open('my-otp.js').read()


def dataize(document, type='text/html'):
    return 'data:%s;base64,%s' % (type, base64.b64encode(document))

def otp_doc(secret):
    key = binascii.hexlify(secret)
    doc = '<html><body>xxx<script type="text/javascript">%s;history.back()</script></body></html>' % (crypto_js + ';' + hotp_js + ';' + myotp_js.replace('FAFA',key))
    return dataize(doc)

if __name__ == '__main__':
    import sys
    print '''
<html>
<body>
<a href="%s">OTP Link</a>
</body>
</html>''' % otp_doc(sys.argv[1])
