class Fink:
    
    @classmethod
    def encode(cls, msg: str, step: int) -> str:
        res = []
        zeros = "0"*(2*step + 1)
        msg = zeros + msg + zeros
        for i in range(len(msg)):
            res.append(msg[i])
            if step <= i < len(msg)-step-1:
                res.append(str(int(msg[i-step]) ^ int(msg[i+step+1])))
            else:
                res.append("0")

        return "".join(res)
    
    
    @classmethod
    def decode(cls, msg: str, step: int) -> str:
        msgSize = len(msg)//2 - (2*step + 1) * 2
        a = [int(msg[i]) for i in range(len(msg)) if i%2==0]
        b = [int(msg[i]) for i in range(len(msg)) if i%2==1]
        
        for i in range(msgSize):
            if i < len(a) - (4*step+2):
                if ((a[i] ^ a[i+2*step+1]) != b[i+step] and 
                    (a[i+2*step+1] ^ a[i+4*step+2]) != b[i+3*step+1]):
                    a[i+2*step+1] = (a[i+2*step+1] + 1)%2
        
        return "".join(map(str, a))[2*step+1:len(a)-2*step-1]