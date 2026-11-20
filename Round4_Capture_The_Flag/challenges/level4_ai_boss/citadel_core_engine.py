# ==============================================================================
# AEGIS CYBER OPERATIONS // LEVEL 4: THE CITADEL CORE VIRTUAL MACHINE
# TARGET: Custom Micro-VM Execution & Algorithmic Constraint Solver
# RULE: 🤖 AI SANCTION GRANTED!
#       You are authorized to use Generative AI (ChatGPT, Claude, Gemini)
#       to reverse-engineer this virtual machine and compute the master access key.
# ==============================================================================

import sys

TARGET_STATE_REGISTER = [
    238, 132, 79, 115, 79, 139, 141, 80, 242, 199, 143, 220, 
    92, 29, 161, 46, 230, 101, 83, 184, 39, 102, 236, 59, 
    255, 50, 164, 247, 187, 56, 176, 206, 227, 107, 8, 80
]

class MicroVM:
    """
    Simulated 8-bit Micro-Virtual Machine Architecture.
    Executes a 4-stage pipeline per input byte using dynamic key schedules.
    """
    @staticmethod
    def _rotl8(val, shift):
        return ((val << shift) & 0xFF) | ((val & 0xFF) >> (8 - shift))

    @staticmethod
    def process_byte(byte_val, cycle_index):
        # Stage 1: Primary Non-Linear Key Schedule XOR
        k1 = ((cycle_index * 41) + 137) % 256
        s1 = byte_val ^ k1
        
        # Stage 2: 4-bit Circular Left Barrel Shifter
        s2 = MicroVM._rotl8(s1, 4)
        
        # Stage 3: Modular Affine Additive Transform
        s3 = (s2 + 73) % 256
        
        # Stage 4: Secondary Dynamic Key Schedule XOR
        k2 = ((cycle_index * 17) + 59) % 256
        s4 = s3 ^ k2
        return s4

def verify_citadel_key(candidate_flag):
    if len(candidate_flag) != len(TARGET_STATE_REGISTER):
        return False

    transformed_registers = []
    for idx, ch in enumerate(candidate_flag):
        transformed_registers.append(MicroVM.process_byte(ord(ch), idx))

    return transformed_registers == TARGET_STATE_REGISTER

def main():
    print("===========================================================")
    print("⚡ AEGIS CYBER DEFENSE // CITADEL CORE MICRO-VM VALIDATOR")
    print("===========================================================")
    print("[i] AI PROTOCOLS AUTHORIZED (ChatGPT / Claude / Gemini).")
    print("[i] Task: Reverse the 4-stage MicroVM logic to extract the master flag.\n")

    try:
        user_input = input("Enter Citadel Master Key: ").strip()
    except (KeyboardInterrupt, EOFError):
        sys.exit(0)

    if verify_citadel_key(user_input):
        print("\n[+] 🟢 MASTER AUTHENTICATION ACCEPTED!")
        print(f"[+] SUBMIT THIS FLAG TO THE CTF DASHBOARD: {user_input}")
    else:
        print("\n[-] 🔴 ACCESS DENIED: Register state mismatch.")

if __name__ == '__main__':
    main()
