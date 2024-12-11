from convolution import Fink
import matplotlib.pyplot as plt

def main():
    inputMessage = "10010111001011"

    # Test for 2 errors
    errors = {}
    encoded = Fink.encode(inputMessage, 0)
    print(encoded[::-1])
    for i in range(len(encoded)-1):
        # First error in message
        encodedErrored = list(encoded)
        encodedErrored[i] = "0" if encodedErrored[i] == "1" else "1"
        encodedErrored = "".join(encodedErrored)
        for k in range(i+1, len(encoded)):
            # Second error in message
            encodedErrored = list(encodedErrored)
            encodedErrored[k] = "0" if encodedErrored[k] == "1" else "1"
            encodedErrored = "".join(encodedErrored)
            decoded = Fink.decode(encodedErrored, 0)
            curErrorsIdxs = []
            for j in range(len(decoded)):
                if decoded[j] != inputMessage[j]:
                    curErrorsIdxs.append(j)
            errors[(i,k)] = curErrorsIdxs
            encodedErrored = list(encodedErrored)
            encodedErrored[k] = "0" if encodedErrored[k] == "1" else "1"
            encodedErrored = "".join(encodedErrored)
    for key, value in errors.items():
        if value:
            print(f"Errors in the encoded message by indexes {key} led to errors in decoding by indexes {value}")
        
    # Test for 1 error     
    fig = plt.figure(figsize=(15, 10))
        
    for step in range(8):
        encoded = Fink.encode(inputMessage, step)
        print(f"Step {step}, Encoded message: {encoded}")

        res = []

        for i in range(len(encoded)):
            # Error in message
            encodedErrored = list(encoded)
            encodedErrored[i] = "0" if encodedErrored[i] == "1" else "1"
            encodedErrored = "".join(encodedErrored)
            decoded = Fink.decode(encodedErrored, step)
            curErrorsIdxs = []
            for j in range(len(decoded)):
                if decoded[j] != inputMessage[j]:
                    curErrorsIdxs.append(j)
            res.append(curErrorsIdxs)

        # Prepare data for visualization
        x = []
        y = []
        for i, errorsIxds in enumerate(res):
            for error in errorsIxds:
                x.append(i)
                y.append(error)

        # Plot the results for current step
        ax1 = fig.add_subplot(2,4,step + 1)
        ax1.scatter(x, y, label=f"Step {step}", alpha=0.6)
        ax1.set_title(f"Step = {step}")
        ax1.set_xlim([0, len(encoded)])
        ax1.set_ylim([0, len(inputMessage)])
        plt.xlabel("Error Position in Encoded Message")
        plt.ylabel("Error Position in Decoded Message")
        ax1.grid(True)
    
    plt.tight_layout()
    plt.show()
    


if __name__ == "__main__":
    main()