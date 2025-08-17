window.addEventListener('load', () => {
    const connectButton = document.getElementById('connectButton');
    const walletAddress = document.getElementById('walletAddress');

    connectButton.addEventListener('click', connectWallet);

    async function connectWallet() {
        if (typeof window.ethereum !== 'undefined') {
            try {
                // Create a new Web3Provider from the browser's Ethereum provider
                const provider = new ethers.providers.Web3Provider(window.ethereum);

                // Request account access
                await provider.send("eth_requestAccounts", []);

                // Get the signer (the user's account)
                const signer = provider.getSigner();

                // Get the user's address
                const address = await signer.getAddress();

                // Display the address
                // Shorten the address for better display: 0x1234...abcd
                const shortAddress = `${address.substring(0, 6)}...${address.substring(address.length - 4)}`;
                walletAddress.textContent = `Connected: ${shortAddress}`;

                // Update the button
                connectButton.textContent = 'Connected';
                connectButton.disabled = true;

            } catch (error) {
                console.error("User rejected request or an error occurred:", error);
                walletAddress.textContent = "Connection failed. Please try again.";
            }
        } else {
            // If MetaMask is not installed
            walletAddress.textContent = "No wallet detected. Please install MetaMask!";
            connectButton.disabled = true;
        }
    }
});
