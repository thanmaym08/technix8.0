# ==============================================================================
# AEGIS CYBER OPERATIONS // LEVEL 4 MASTER SOLVER
# Reverse Algorithm for citadel_core_engine.py MicroVM
# ==============================================================================

TARGET_STATE_REGISTER = [
    238, 132, 79, 115, 79, 139, 141, 80, 242, 199, 143, 220, 
    92, 29, 161, 46, 230, 101, 83, 184, 39, 102, 236, 59, 
    255, 50, 164, 247, 187, 56, 176, 206, 227, 107, 8, 80
]

def _rotr8(val, shift):
    """8-bit circular right bitwise rotation (reverse of _rotl8)."""
    return ((val >> shift) & 0xFF) | (((val & 0xFF) << (8 - shift)) & 0xFF)

def solve():
    recovered_chars = []
    for idx, s4 in enumerate(TARGET_STATE_REGISTER):
        # 1. Reverse Stage 4: Secondary Dynamic Key Schedule XOR
        k2 = ((idx * 17) + 59) % 256
        s3 = s4 ^ k2
        
        # 2. Reverse Stage 3: Modular Affine Additive Transform (-73 mod 256)
        s2 = (s3 - 73) % 256
        
        # 3. Reverse Stage 2: 4-bit Circular Right Barrel Shifter
        s1 = _rotr8(s2, 4)
        
        # 4. Reverse Stage 1: Primary Non-Linear Key Schedule XOR
        k1 = ((idx * 41) + 137) % 256
        orig_byte = s1 ^ k1
        
        recovered_chars.append(chr(orig_byte))

    return ''.join(recovered_chars)

if __name__ == '__main__':
    flag = solve()
    print('[+] Level 4 Master Key Successfully Recovered:')
    print(f'    {flag}')
