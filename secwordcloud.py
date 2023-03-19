
from wordcloud import WordCloud
import random

# Define a list of cyber security words
words = [
    "VPN", 
    "Firewall", 
    "PenetrationTesting", 
    "Malware", 
    "SocialEngineering", 
    "IntrusionDetection", 
    "VPN",
    "Firewall",
    "Antivirus",
    "Malware",
    "Phishing",
    "BruteForce",
    "IntrusionDetection",
    "DataBreach",
    "PenetrationTesting",
    "Encryption",
    "TwoFactorAuthentication",
    "Cybersecurity",
    "Hacker",
    "Adware",
    "Backdoor",
    "SocialEngineering",
    "Ransomware",
    "ZeroDay",
    "Rootkit",
    "Trojan",
    "Worm",
    "Botnet",
    "Bluesnarfing",
    "Blockchain",
    "DeepPacketInspection",
    "DeceptionTechnology",
    "DataLossPrevention",
    "AccessControl",
    "Authentication",
    "DenialOfService",
    "Exploit",
    "Vulnerability",
    "PatchManagement",
    "IdentityTheft",
    "SecurityAudit",
    "RiskAssessment",
    "SecurityPolicy",
    "SecurityAwarenessTraining",
    "ThreatIntelligence",
    "NetworkSecurity",
    "EndpointSecurity",
    "ApplicationSecurity",
    "Protocol",
"Ransomware",
"RedTeam",
"RiskAssessment",
"Rootkit",
"Salting",
"Scareware",
"SecureSocketsLayer",
"SecurityAwareness",
"Session Hijacking",
"Smishing",
"SocialEngineering",
"Spam",
"Spyware",
"SSLCertificate",
"Steganography",
"StrongAuthentication",
"SystemIntegrity",
"ThreatIntelligence",
"TrojanHorse",
"Virus",
"VPN",
"Vulnerability",
"WAF",
"Worm",
"Zero-Day",
    "DataBreach",
    "DDoS",
    "Domain",
    "Encryption",
    "Exploit",
    "Firewall",
    "Hacker",
    "IdentityTheft",
    "Keylogger",
    "Malware",
    "Phishing",
    "Ransomware",
    "Spam",
    "Spyware",
    "TrojanHorse",
    "CloudSecurity",
    "MobileDeviceSecurity",
    "DatabaseSecurity",
    "WebSecurity",
    "WirelessSecurity",
    "PhysicalSecurity",
    "IncidentResponse",
    "DisasterRecovery",
    "BusinessContinuity",
    "CyberInsurance",
    "Compliance",
    "GDPR",
    "HIPAA",
    "PCI",
    "ISO27001",
    "NIST",
    "SOC" , 
    "Encryption", 
    "Hacker", 
    "Phishing", 
    "TwoFactorAuthentication"
]

for i in range(10):
    # Randomly select 50 words from the list
    selected_words = random.sample(words, 100)

    # Join the selected words into a single string
    text = ' '.join(selected_words)

    # Define a function to generate random colors for each word
    def random_color_func(word=None, font_size=None, position=None,
                          orientation=None, font_path=None, random_state=None):
        # Generate a random hue value between 0 and 255
        h = random.randint(0, 255)
        # Generate a random saturation value between 50% and 100%
        s = random.randint(50, 100)
        # Generate a lightness value between 30% and 70%
        l = int(100 * float(random_state.randint(60, 140)) / 255.0)

        # Return the color in HSL format as a string
        return f"hsl({h}, {s}%, {l}%)"

    # Define a random background color
    bg_color = f"rgb({random.randint(0, 255)}, {random.randint(0, 255)}, {random.randint(0, 255)})"

    # Define a random filename for each iteration
    filename = f"cyber_security_words_{i}.png"

    # Create a WordCloud object with custom parameters
    wc = WordCloud(background_color=bg_color, max_words=100,
                   width=800, height=600,
                   prefer_horizontal=0.5,
                   relative_scaling=0.5,
                   color_func=random_color_func)

    # Generate the word cloud from the text
    wc.generate(text)

    # Save the word cloud as an image file
    wc.to_file(filename)
