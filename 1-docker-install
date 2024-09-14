Here’s a step-by-step guide to installing Docker on Windows, macOS, and Linux (using a common distribution like Ubuntu). Follow the instructions according to your operating system.

---

## **1. Installing Docker on Windows**

### **Prerequisites:**
- **Windows 10 64-bit**: Pro, Enterprise, or Education (Build 19041 or later).
- **Windows 11** is also supported.

### **Steps**:

1. **Download Docker Desktop**:
   - Visit the Docker website and download Docker Desktop for Windows from [here](https://www.docker.com/products/docker-desktop).

2. **Install Docker Desktop**:
   - Run the downloaded installer (`Docker Desktop Installer.exe`).
   - Follow the instructions in the installation wizard.

3. **Enable WSL 2 (Windows Subsystem for Linux 2)**:
   - Open PowerShell as Administrator and run the following command to enable WSL:
     ```bash
     wsl --install
     ```
   - Restart your machine if required.

4. **Configure Docker to use WSL 2**:
   - Open Docker Desktop and go to **Settings** > **General**.
   - Check the box that says "Use the WSL 2 based engine."

5. **Start Docker Desktop**:
   - Launch Docker Desktop from the Start menu.
   - Once started, Docker will run in the background and be ready to use.

6. **Verify Installation**:
   - Open **PowerShell** or **Command Prompt** and run:
     ```bash
     docker --version
     ```

---

## **2. Installing Docker on macOS**

### **Prerequisites:**
- **macOS 10.15 (Catalina)** or newer is required.

### **Steps**:

1. **Download Docker Desktop**:
   - Visit the Docker website and download Docker Desktop for Mac from [here](https://www.docker.com/products/docker-desktop).

2. **Install Docker Desktop**:
   - Open the downloaded `.dmg` file and drag the Docker icon to the Applications folder.

3. **Start Docker Desktop**:
   - Launch Docker Desktop from the **Applications** folder.
   - The Docker whale icon will appear in the menu bar, indicating Docker is running.

4. **Verify Installation**:
   - Open **Terminal** and run:
     ```bash
     docker --version
     ```

---

## **3. Installing Docker on Linux (Ubuntu)**

### **Prerequisites:**
- **Ubuntu 18.04** or later.
  
### **Steps**:

1. **Uninstall old versions (if any)**:
   - If you have an older version of Docker installed, remove it first:
     ```bash
     sudo apt remove docker docker-engine docker.io containerd runc
     ```

2. **Update the package database**:
   ```bash
   sudo apt update
   ```

3. **Install necessary packages**:
   ```bash
   sudo apt install apt-transport-https ca-certificates curl software-properties-common
   ```

4. **Add Docker's official GPG key**:
   ```bash
   curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpg
   ```

5. **Set up the stable repository**:
   ```bash
   echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
   ```

6. **Update the package database again**:
   ```bash
   sudo apt update
   ```

7. **Install Docker Engine**:
   ```bash
   sudo apt install docker-ce docker-ce-cli containerd.io
   ```

8. **Start Docker**:
   - Ensure Docker is running by starting the service:
     ```bash
     sudo systemctl start docker
     ```

9. **Enable Docker to start at boot**:
   ```bash
   sudo systemctl enable docker
   ```

10. **Verify Installation**:
    - Check if Docker is installed correctly by running:
      ```bash
      sudo docker --version
      ```

11. **Run Docker without sudo (optional)**:
    - Add your user to the `docker` group to avoid using `sudo` for Docker commands:
      ```bash
      sudo usermod -aG docker $USER
      ```
    - Log out and log back in for the changes to take effect.

---

### **That's it!** Docker is now installed on your system.
