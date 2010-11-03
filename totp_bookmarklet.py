import binascii
import base64
import os.path

def __content(f):
    return open(os.path.join(os.path.dirname(__file__), f)).read()

crypto_js = __content('crypto.js')
hotp_js = __content('hotp.js')
myotp_js = __content('my-otp.js').


def dataize(document, type='text/html'):
    return 'data:%s;base64,%s' % (type, base64.b64encode(document))

def otp_doc(secret):
    key = binascii.hexlify(secret)
    doc = ''''<html>
<body>
<script type="text/javascript">%s;history.back()</script>
</body>
</html>''' % (crypto_js + ';' + hotp_js + ';' + myotp_js.replace('FAFA',key))
    return dataize(doc)

if __name__ == '__main__':
    import sys
    print '''
<html>
<body>
<a href="%s">OTP Link</a>
</body>
</html>''' % otp_doc(sys.argv[1])
