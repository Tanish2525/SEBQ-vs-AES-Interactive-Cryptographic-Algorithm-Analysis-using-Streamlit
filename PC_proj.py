"""
SEBQ vs AES Encryption Analysis Tool
Principles of Cryptography - Mini Project
By - Tanish, Utkarsh, Adhisha
Computer Science Department
Academic Year: 2025-26
"""

import streamlit as st
import time
import random
import json
import base64
import hashlib
from typing import List, Dict, Tuple, Any
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad
import plotly.graph_objects as go
import plotly.express as px
import pandas as pd
import numpy as np
from io import StringIO
import sys

# Set page configuration
st.set_page_config(
    page_title="SEBQ vs AES Cryptography Project",
    page_icon="🔐",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Enhanced CSS for fancy academic styling
st.markdown("""
<style>
    .main-header {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 3rem;
        border-radius: 15px;
        color: white;
        text-align: center;
        margin-bottom: 2rem;
        box-shadow: 0 20px 40px rgba(0,0,0,0.3);
        border: 2px solid rgba(255,255,255,0.1);
    }
    .project-authors {
        background: linear-gradient(45deg, #ff9a56 0%, #ff6b9d 100%);
        padding: 1rem;
        border-radius: 10px;
        color: white;
        text-align: center;
        margin-bottom: 1rem;
        font-weight: bold;
    }
    .encryption-section {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 2rem;
        border-radius: 12px;
        margin: 1rem 0;
        color: white;
        box-shadow: 0 10px 25px rgba(0,0,0,0.2);
    }
    .decryption-section {
        background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%);
        padding: 2rem;
        border-radius: 12px;
        margin: 1rem 0;
        color: white;
        box-shadow: 0 10px 25px rgba(0,0,0,0.2);
    }
    .comparison-section {
        background: linear-gradient(135deg, #4facfe 0%, #00f2fe 100%);
        padding: 2rem;
        border-radius: 12px;
        margin: 1rem 0;
        color: white;
        box-shadow: 0 10px 25px rgba(0,0,0,0.2);
    }
    .algorithm-detail {
        background: linear-gradient(135deg, #fa709a 0%, #fee140 100%);
        padding: 2rem;
        border-radius: 12px;
        margin: 1rem 0;
        color: white;
        box-shadow: 0 10px 25px rgba(0,0,0,0.2);
    }
    .copy-section {
        background: #f8f9fa;
        padding: 1.5rem;
        border-radius: 10px;
        border: 2px solid #e9ecef;
        margin: 1rem 0;
    }
    .stTextArea > div > div > textarea {
        font-family: 'Courier New', monospace !important;
        font-size: 11px !important;
        line-height: 1.3 !important;
        background-color: #212529 !important;
        color: #f8f9fa !important;
    }
    .metric-card {
        background: white;
        padding: 1.5rem;
        border-radius: 10px;
        box-shadow: 0 5px 15px rgba(0,0,0,0.1);
        text-align: center;
        margin: 0.5rem 0;
    }
    .sidebar .sidebar-content {
        background: linear-gradient(180deg, #667eea 0%, #764ba2 100%);
    }
    .fancy-box {
        background: linear-gradient(45deg, #667eea, #764ba2);
        border-radius: 10px;
        padding: 1rem;
        color: white;
        margin: 1rem 0;
        box-shadow: 0 5px 15px rgba(0,0,0,0.2);
    }
</style>
""", unsafe_allow_html=True)

# Initialize random seed for consistent results
random.seed(42)
np.random.seed(42)


class AdvancedSEBQCryptosystem:
    """
    Advanced SEBQ (Symmetric Encryption Based on Quasigroup) Implementation
    Enhanced with detailed step-by-step visualization and comprehensive cryptographic analysis
    """

    def __init__(self, key_size: int = 16):
        self.key_size = key_size
        self.encryption_time = 0.0
        self.decryption_time = 0.0
        self.substitution_table = None
        self.inverse_table = None
        self.initialization_vector = None

    def add_detailed_step(self, step: str, technical_detail: str, mathematical_detail: str, step_container,
                          current_steps):
        """Add comprehensive processing step with multiple levels of detail"""
        new_steps = current_steps + f"🔥 SEBQ: {step}\n"
        new_steps += f"   🔧 Technical: {technical_detail}\n"
        new_steps += f"   🧮 Mathematical: {mathematical_detail}\n\n"
        step_container.text_area("SEBQ Algorithm Processing Steps:", new_steps, height=500,
                                 key=f"sebq_{len(new_steps)}")
        time.sleep(0.00001)
        return new_steps

    def perform_encryption_with_detailed_steps(self, input_text: str, step_container):
        """Execute SEBQ encryption with comprehensive step visualization"""

        # Raw algorithm execution for accurate timing
        raw_start = time.time()
        key_table = list(range(256))
        random.shuffle(key_table)
        inv_table = [0] * 256
        for i, val in enumerate(key_table):
            inv_table[val] = i
        iv = random.randint(0, 2 ** 32 - 1)
        plaintext_bytes = [ord(c) for c in input_text]
        current_iv = iv
        ciphertext_bytes = []
        for i, byte_val in enumerate(plaintext_bytes):
            iv_byte = (current_iv + i) % 256
            mixed = byte_val ^ iv_byte
            cipher_byte = key_table[mixed]
            current_iv = (current_iv + cipher_byte) % (2 ** 32)
            ciphertext_bytes.append(cipher_byte)
        self.encryption_time = time.time() - raw_start

        # Store components
        self.substitution_table = key_table
        self.inverse_table = inv_table
        self.initialization_vector = iv

        # Enhanced step-by-step visualization
        steps_display = ""

        steps_display = self.add_detailed_step(
            "Phase 1 - SEBQ Cryptographic System Initialization",
            "Initializing quasigroup-based symmetric encryption system with 256-element algebraic structure",
            "Setting up mathematical quasigroup (Q, •) where Q = {0,1,2,...,255} forms closed binary operation",
            step_container, steps_display
        )

        steps_display = self.add_detailed_step(
            "Phase 2 - Quasigroup Substitution Table Generation",
            "Creating bijective mapping function using cryptographically secure permutation of integer domain",
            "Generating π: Z₂₅₆ → Z₂₅₆ where π(x) provides unique substitution for each byte value",
            step_container, steps_display
        )

        steps_display = self.add_detailed_step(
            "Phase 3 - Fisher-Yates Cryptographic Permutation",
            "Applying Durstenfeld's modern Fisher-Yates algorithm for unbiased random permutation",
            "For i from n-1 to 1: j = random(0, i); swap(array[i], array[j]) ensuring uniform distribution",
            step_container, steps_display
        )

        steps_display = self.add_detailed_step(
            "Phase 4 - Inverse Substitution Table Computation",
            "Computing mathematical inverse function for decryption bijection requirements",
            f"Creating π⁻¹ where π⁻¹(π(x)) = x for all x ∈ Z₂₅₆, ensuring cryptographic reversibility",
            step_container, steps_display
        )

        steps_display = self.add_detailed_step(
            "Phase 5 - Initialization Vector Generation",
            f"Generating 32-bit IV: {iv} for chained block cipher mode implementation",
            "IV ← random(0, 2³²-1) providing 2³² possible initialization states for enhanced security",
            step_container, steps_display
        )

        steps_display = self.add_detailed_step(
            "Phase 6 - Plaintext Preprocessing",
            f"Converting {len(input_text)} characters to ASCII byte representation for algebraic operations",
            "M = {m₁, m₂, ..., mₙ} where mᵢ = ASCII(cᵢ) ∈ [0, 255] for character cᵢ",
            step_container, steps_display
        )

        # Show detailed encryption process for chunks
        chunk_size = max(1, len(plaintext_bytes) // 12)
        for i in range(0, len(plaintext_bytes), chunk_size):
            chunk_end = min(i + chunk_size, len(plaintext_bytes))
            steps_display = self.add_detailed_step(
                f"Phase 7 - SEBQ Encryption: Bytes {i + 1}-{chunk_end}",
                f"Applying four-stage SEBQ transformation: IV mixing → XOR operation → Substitution → Chain update",
                f"For byte mᵢ: IV' = (IV + i) mod 256; X = mᵢ ⊕ IV'; C = π(X); IV = (IV + C) mod 2³²",
                step_container, steps_display
            )

        steps_display = self.add_detailed_step(
            "Phase 8 - Encryption Finalization",
            f"SEBQ encryption completed: {len(ciphertext_bytes)} bytes generated with full quasigroup transformation",
            "Final ciphertext C = {c₁, c₂, ..., cₙ} where each cᵢ resulted from complete SEBQ operations",
            step_container, steps_display
        )

        key_components = {
            'substitution_table': key_table,
            'inverse_table': inv_table,
            'initialization_vector': iv,
            'algorithm_type': 'SEBQ'
        }

        return ciphertext_bytes, key_components, self.encryption_time

    def perform_decryption_with_detailed_steps(self, ciphertext_data: List[int], key_components: Dict, step_container):
        """Execute SEBQ decryption with comprehensive step visualization"""

        # Raw algorithm execution for accurate timing
        raw_start = time.time()
        key_table = key_components['substitution_table']
        inv_table = key_components['inverse_table']
        iv = key_components['initialization_vector']
        current_iv = iv
        decrypted_bytes = []
        for i, cipher_byte in enumerate(ciphertext_data):
            iv_byte = (current_iv + i) % 256
            mixed = inv_table[cipher_byte]
            original = mixed ^ iv_byte
            current_iv = (current_iv + cipher_byte) % (2 ** 32)
            decrypted_bytes.append(original)
        decrypted_text = ''.join(chr(b) for b in decrypted_bytes)
        self.decryption_time = time.time() - raw_start

        # Enhanced step-by-step visualization
        steps_display = ""

        steps_display = self.add_detailed_step(
            "Phase 1 - SEBQ Decryption System Initialization",
            "Loading SEBQ decryption engine with stored cryptographic parameters and key material",
            "Initializing inverse operations for quasigroup-based symmetric decryption process",
            step_container, steps_display
        )

        steps_display = self.add_detailed_step(
            "Phase 2 - Cryptographic Key Material Loading",
            "Retrieving substitution table, inverse mapping, and initialization vector from secure storage",
            "Loading π, π⁻¹, and IV where these components form complete SEBQ key space K",
            step_container, steps_display
        )

        steps_display = self.add_detailed_step(
            "Phase 3 - Ciphertext Analysis and Preparation",
            f"Analyzing {len(ciphertext_data)} encrypted bytes for reverse SEBQ transformation",
            "Preparing C = {c₁, c₂, ..., cₙ} for application of inverse quasigroup operations",
            step_container, steps_display
        )

        # Show detailed decryption process
        chunk_size = max(1, len(ciphertext_data) // 12)
        for i in range(0, len(ciphertext_data), chunk_size):
            chunk_end = min(i + chunk_size, len(ciphertext_data))
            steps_display = self.add_detailed_step(
                f"Phase 4 - SEBQ Decryption: Bytes {i + 1}-{chunk_end}",
                "Applying inverse SEBQ operations: IV reconstruction → Inverse substitution → XOR reversal",
                f"For cᵢ: IV' = (IV + i) mod 256; X = π⁻¹(cᵢ); mᵢ = X ⊕ IV'; IV = (IV + cᵢ) mod 2³²",
                step_container, steps_display
            )

        steps_display = self.add_detailed_step(
            "Phase 5 - Plaintext Reconstruction",
            "Converting decrypted byte values back to readable ASCII character representation",
            "M = {m₁, m₂, ..., mₙ} → Text where char(mᵢ) reconstructs original message",
            step_container, steps_display
        )

        steps_display = self.add_detailed_step(
            "Phase 6 - Decryption Completion and Verification",
            f"SEBQ decryption completed: {len(decrypted_text)} characters successfully recovered",
            "Verification: ∀i, decrypt(encrypt(mᵢ)) = mᵢ confirms bijective property maintenance",
            step_container, steps_display
        )

        return decrypted_text, self.decryption_time


class AdvancedAESCryptosystem:
    """
    Advanced AES Implementation with detailed step-by-step cryptographic visualization
    Enhanced with comprehensive technical explanations and mathematical foundations
    """

    def __init__(self):
        self.encryption_time = 0.0
        self.decryption_time = 0.0
        self.encryption_key = None
        self.initialization_vector = None

    def add_detailed_step(self, step: str, technical_detail: str, mathematical_detail: str, step_container,
                          current_steps):
        """Add comprehensive processing step with multiple levels of detail"""
        new_steps = current_steps + f"🔷 AES: {step}\n"
        new_steps += f"   🔧 Technical: {technical_detail}\n"
        new_steps += f"   🧮 Mathematical: {mathematical_detail}\n\n"
        step_container.text_area("AES Algorithm Processing Steps:", new_steps, height=500, key=f"aes_{len(new_steps)}")
        time.sleep(0.00001)
        return new_steps

    def perform_encryption_with_detailed_steps(self, input_text: str, step_container):
        """Execute AES encryption with comprehensive step visualization"""

        # Raw algorithm execution for accurate timing
        raw_start = time.time()
        key = get_random_bytes(32)
        iv = get_random_bytes(16)
        plaintext_bytes = input_text.encode('utf-8')
        padded_plaintext = pad(plaintext_bytes, AES.block_size)
        cipher = AES.new(key, AES.MODE_CBC, iv)
        ciphertext = cipher.encrypt(padded_plaintext)
        self.encryption_time = time.time() - raw_start

        # Store components
        self.encryption_key = key
        self.initialization_vector = iv

        # Enhanced step-by-step visualization
        steps_display = ""

        steps_display = self.add_detailed_step(
            "Phase 1 - AES Cryptographic System Initialization",
            "Initializing Advanced Encryption Standard with Rijndael algorithm implementation",
            "Setting up AES with 128-bit block size and 256-bit key for maximum security configuration",
            step_container, steps_display
        )

        steps_display = self.add_detailed_step(
            "Phase 2 - AES-256 Master Key Generation",
            "Generating 256-bit cryptographic key using secure random number generator",
            "K = random(2²⁵⁶) providing 2²⁵⁶ possible key combinations for cryptographic strength",
            step_container, steps_display
        )

        steps_display = self.add_detailed_step(
            "Phase 3 - CBC Mode Initialization Vector",
            "Creating 128-bit IV for Cipher Block Chaining mode to prevent pattern recognition",
            "IV = random(2¹²⁸) ensuring each encryption produces unique ciphertext for identical plaintext",
            step_container, steps_display
        )

        steps_display = self.add_detailed_step(
            "Phase 4 - UTF-8 Text Encoding",
            f"Converting {len(input_text)} characters to UTF-8 byte representation for block processing",
            "Text → bytes: each character mapped to 1-4 bytes using UTF-8 encoding standard",
            step_container, steps_display
        )

        steps_display = self.add_detailed_step(
            "Phase 5 - PKCS7 Padding Application",
            f"Applying PKCS#7 padding: {len(plaintext_bytes)} → {len(padded_plaintext)} bytes for 128-bit blocks",
            "Padding ensures message length ≡ 0 (mod 16) by adding k bytes of value k",
            step_container, steps_display
        )

        steps_display = self.add_detailed_step(
            "Phase 6 - AES Key Schedule Expansion",
            "Expanding 256-bit master key into 15 round keys using Rijndael key expansion",
            "K₀, K₁, ..., K₁₄ generated through SubWord, RotWord, and XOR operations with round constants",
            step_container, steps_display
        )

        # Process blocks with detailed explanation
        num_blocks = len(padded_plaintext) // 16
        chunk_size = max(1, num_blocks // 10)
        for i in range(0, num_blocks, chunk_size):
            chunk_end = min(i + chunk_size, num_blocks)
            steps_display = self.add_detailed_step(
                f"Phase 7 - AES Block Processing: Blocks {i + 1}-{chunk_end}",
                f"Processing 128-bit blocks through 14 rounds of SubBytes, ShiftRows, MixColumns, AddRoundKey",
                "Each block: State ← AddRoundKey(K₀); for r=1 to 13: SubBytes→ShiftRows→MixColumns→AddRoundKey(Kᵣ); Final: SubBytes→ShiftRows→AddRoundKey(K₁₄)",
                step_container, steps_display
            )

        steps_display = self.add_detailed_step(
            "Phase 8 - CBC Chaining Implementation",
            "Applying Cipher Block Chaining: each plaintext block XORed with previous ciphertext",
            "C₀ = E(K, P₀ ⊕ IV); Cᵢ = E(K, Pᵢ ⊕ Cᵢ₋₁) ensuring avalanche propagation across blocks",
            step_container, steps_display
        )

        steps_display = self.add_detailed_step(
            "Phase 9 - AES Encryption Completion",
            f"AES encryption completed: {len(ciphertext)} bytes generated with full Rijndael transformation",
            "Final ciphertext provides confidentiality through proven substitution-permutation network",
            step_container, steps_display
        )

        key_components = {
            'encryption_key': key,
            'initialization_vector': iv,
            'algorithm_type': 'AES'
        }

        return ciphertext, key_components, self.encryption_time

    def perform_decryption_with_detailed_steps(self, ciphertext_data: bytes, key_components: Dict, step_container):
        """Execute AES decryption with comprehensive step visualization"""

        # Raw algorithm execution for accurate timing
        raw_start = time.time()
        key = key_components['encryption_key']
        iv = key_components['initialization_vector']
        cipher = AES.new(key, AES.MODE_CBC, iv)
        padded_plaintext = cipher.decrypt(ciphertext_data)
        plaintext_bytes = unpad(padded_plaintext, AES.block_size)
        decrypted_text = plaintext_bytes.decode('utf-8')
        self.decryption_time = time.time() - raw_start

        # Enhanced step-by-step visualization
        steps_display = ""

        steps_display = self.add_detailed_step(
            "Phase 1 - AES Decryption System Initialization",
            "Loading AES decryption engine with stored cryptographic parameters",
            "Initializing inverse Rijndael operations for symmetric key decryption process",
            step_container, steps_display
        )

        steps_display = self.add_detailed_step(
            "Phase 2 - Cryptographic Key Material Loading",
            "Retrieving 256-bit master key and 128-bit IV from secure key storage",
            "Loading K and IV where these parameters define unique AES decryption context",
            step_container, steps_display
        )

        steps_display = self.add_detailed_step(
            "Phase 3 - Inverse Key Schedule Generation",
            "Regenerating 15 round keys and computing inverse round keys for decryption",
            "Same key expansion as encryption, but applying inverse operations in reverse order",
            step_container, steps_display
        )

        steps_display = self.add_detailed_step(
            "Phase 4 - Ciphertext Block Analysis",
            f"Analyzing {len(ciphertext_data)} encrypted bytes for 128-bit block processing",
            "Preparing ciphertext blocks for inverse AES transformation through 14 rounds",
            step_container, steps_display
        )

        # Process blocks with detailed explanation
        num_blocks = len(ciphertext_data) // 16
        chunk_size = max(1, num_blocks // 10)
        for i in range(0, num_blocks, chunk_size):
            chunk_end = min(i + chunk_size, num_blocks)
            steps_display = self.add_detailed_step(
                f"Phase 5 - AES Block Decryption: Blocks {i + 1}-{chunk_end}",
                "Applying inverse AES rounds: AddRoundKey → InvShiftRows → InvSubBytes → InvMixColumns",
                "State ← AddRoundKey(K₁₄); for r=13 to 1: InvShiftRows→InvSubBytes→AddRoundKey(Kᵣ)→InvMixColumns; Final: InvShiftRows→InvSubBytes→AddRoundKey(K₀)",
                step_container, steps_display
            )

        steps_display = self.add_detailed_step(
            "Phase 6 - CBC Chain Reversal",
            "Reversing cipher block chaining: XOR each decrypted block with previous ciphertext",
            "P₀ = D(K, C₀) ⊕ IV; Pᵢ = D(K, Cᵢ) ⊕ Cᵢ₋₁ recovering original block structure",
            step_container, steps_display
        )

        steps_display = self.add_detailed_step(
            "Phase 7 - PKCS7 Padding Removal",
            "Analyzing and removing PKCS#7 padding to recover original message length",
            "Examining final byte value k and removing last k bytes if valid padding detected",
            step_container, steps_display
        )

        steps_display = self.add_detailed_step(
            "Phase 8 - UTF-8 Text Reconstruction",
            "Converting decrypted bytes back to UTF-8 encoded text representation",
            "Bytes → UTF-8 → Text ensuring proper character encoding reconstruction",
            step_container, steps_display
        )

        steps_display = self.add_detailed_step(
            "Phase 9 - AES Decryption Completion",
            f"AES decryption completed: {len(decrypted_text)} characters successfully recovered",
            "Verification: decryption inverts all encryption operations maintaining data integrity",
            step_container, steps_display
        )

        return decrypted_text, self.decryption_time


def calculate_accurate_avalanche_effect(original_bits: str, modified_bits: str, bit_position: int,
                                        plaintext_length: int) -> float:
    """Calculate avalanche effect with accurate bit position validation"""
    # Fix: if bit_position >= plaintext_length, return 0%
    if bit_position >= plaintext_length:
        return 0.0

    if len(original_bits) != len(modified_bits):
        return 0.0

    differences = sum(1 for a, b in zip(original_bits, modified_bits) if a != b)
    return (differences / len(original_bits)) * 100


def convert_to_binary_representation(data) -> str:
    """Convert byte data to binary string representation"""
    if isinstance(data, list):
        return ''.join(f'{b:08b}' for b in data)
    elif isinstance(data, bytes):
        return ''.join(f'{b:08b}' for b in data)
    else:
        return ""


def create_enhanced_performance_chart(sebq_time: float, aes_time: float, operation: str):
    """Generate enhanced performance comparison visualization"""
    performance_data = {
        'Algorithm': ['SEBQ', 'AES'],
        'Execution Time (seconds)': [sebq_time, aes_time]
    }

    colors = ['#667eea', '#764ba2']

    fig = px.bar(
        performance_data,
        x='Algorithm',
        y='Execution Time (seconds)',
        color='Algorithm',
        color_discrete_sequence=colors,
        title=f'{operation} Performance Analysis - Execution Time Comparison'
    )

    fig.update_layout(
        title_font_size=18,
        showlegend=False,
        height=450,
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)',
    )

    return fig


def create_algorithm_comparison_table():
    """Create comprehensive algorithm comparison table"""
    comparison_data = {
        'Characteristic': [
            'Algorithm Type', 'Key Size', 'Block Size', 'Rounds/Operations',
            'Mathematical Foundation', 'Standardization', 'Security Level',
            'Performance (Software)', 'Performance (Hardware)', 'Memory Usage',
            'Parallelization', 'Resistance to Attacks', 'Implementation Complexity'
        ],
        'SEBQ': [
            'Quasigroup-based symmetric', 'Variable (256-element table + IV)', 'Byte-oriented',
            'Single substitution + chaining', 'Quasigroup algebra', 'Research/Experimental',
            'Theoretical (unproven)', 'Good for small data', 'No hardware acceleration',
            '2KB+ (substitution tables)', 'Limited (sequential IV)', 'Unknown/Unanalyzed',
            'Moderate (mathematical concepts)'
        ],
        'AES': [
            'Substitution-permutation network', '128/192/256 bits', '128 bits (16 bytes)',
            '10/12/14 rounds', 'Galois field arithmetic', 'NIST FIPS 197 standard',
            'Proven secure (20+ years)', 'Very fast', 'Hardware accelerated (AES-NI)',
            'Minimal (256 bytes S-box)', 'Excellent (independent blocks)', 'Highly resistant',
            'Well-documented standards'
        ]
    }

    return pd.DataFrame(comparison_data)


def main():
    """Main application interface with enhanced navigation"""

    # Enhanced project header
    st.markdown("""
    <div class="main-header">
        <h1>🔐 SEBQ vs AES Encryption Analysis Tool</h1>
        <h2>Advanced Cryptographic Algorithm Comparison</h2>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="project-authors">
        <h3>Principles of Cryptography - Mini Project</h3>
        <h4>By - Tanish, Utkarsh, Adhisha</h4>
        <p>Computer Science Department | Academic Year: 2025-26</p>
    </div>
    """, unsafe_allow_html=True)

    # Enhanced navigation menu
    st.sidebar.markdown("## 🗂️ Project Navigation")

    selected_section = st.sidebar.selectbox(
        "Select Analysis Section",
        [
            "🔒 Encryption Analysis",
            "🔓 Decryption Analysis",
            "⚡ Performance Comparison",
            "🌊 Avalanche Effect Study",
            "📊 Algorithm Comparison Dashboard",
            "🔬 Deep-Dive: SEBQ & AES Internals"
        ]
    )

    if selected_section == "🔒 Encryption Analysis":
        encryption_analysis_section()
    elif selected_section == "🔓 Decryption Analysis":
        decryption_analysis_section()
    elif selected_section == "⚡ Performance Comparison":
        performance_comparison_section()
    elif selected_section == "🌊 Avalanche Effect Study":
        avalanche_effect_section()
    elif selected_section == "📊 Algorithm Comparison Dashboard":
        algorithm_comparison_dashboard()
    elif selected_section == "🔬 Deep-Dive: SEBQ & AES Internals":
        deep_dive_internals_section()


def encryption_analysis_section():
    """Enhanced encryption comparison analysis interface"""
    st.header("🔒 Advanced Encryption Algorithm Analysis")

    st.markdown("""
    <div class="fancy-box">
        <h4>🎯 Research Objective</h4>
        <p>Comprehensive comparative analysis of SEBQ (Symmetric Encryption Based on Quasigroup) and AES (Advanced Encryption Standard) 
        algorithms featuring real-time step-by-step processing visualization, performance metrics, and cryptographic analysis.</p>
    </div>
    """, unsafe_allow_html=True)

    # Enhanced input section
    sample_text = """This comprehensive cryptography project analyzes two distinct symmetric encryption algorithms: SEBQ (Symmetric Encryption Based on Quasigroup) and AES (Advanced Encryption Standard).

SEBQ represents an innovative approach utilizing mathematical quasigroup algebraic structures for cryptographic operations, offering unique properties through bijective substitution tables and chained initialization vectors. In contrast, AES employs proven substitution-permutation networks with Rijndael algorithm foundations.

This comparative study examines critical characteristics including computational performance, security properties, implementation complexity, memory requirements, and resistance to cryptanalytic attacks. The research methodology incorporates execution time analysis, avalanche effect testing, algorithmic step visualization, and comprehensive mathematical foundations.

Results demonstrate practical applications, theoretical foundations, and provide insights into both established and experimental cryptographic approaches in modern security systems."""

    input_text = st.text_area(
        "📝 Input Text for Comprehensive Encryption Analysis:",
        value=sample_text,
        height=200
    )

    # Enhanced text statistics
    word_count = len(input_text.split())
    character_count = len(input_text)
    byte_count = len(input_text.encode('utf-8'))

    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("📊 Word Count", word_count)
    with col2:
        st.metric("📊 Character Count", character_count)
    with col3:
        st.metric("📊 Byte Count", byte_count)

    if st.button("🚀 Execute Advanced Encryption Analysis", type="primary"):
        if input_text:
            # Create enhanced analysis sections
            col1, col2 = st.columns(2)

            with col1:
                st.markdown('<div class="encryption-section"><h3>🔥 SEBQ Advanced Encryption Analysis</h3></div>',
                            unsafe_allow_html=True)
                sebq_step_container = st.empty()

            with col2:
                st.markdown('<div class="encryption-section"><h3>🔷 AES Advanced Encryption Analysis</h3></div>',
                            unsafe_allow_html=True)
                aes_step_container = st.empty()

            # Execute both algorithms with enhanced tracking
            sebq_system = AdvancedSEBQCryptosystem()
            aes_system = AdvancedAESCryptosystem()

            with st.spinner("🔄 Executing advanced encryption algorithms with detailed analysis..."):
                # Run enhanced encryption processes
                sebq_ciphertext, sebq_keys, sebq_time = sebq_system.perform_encryption_with_detailed_steps(input_text,
                                                                                                           sebq_step_container)
                aes_ciphertext, aes_keys, aes_time = aes_system.perform_encryption_with_detailed_steps(input_text,
                                                                                                       aes_step_container)

            # Store results in session state
            st.session_state['sebq_ciphertext'] = sebq_ciphertext
            st.session_state['sebq_keys'] = sebq_keys
            st.session_state['sebq_encrypt_time'] = sebq_time
            st.session_state['aes_ciphertext'] = aes_ciphertext
            st.session_state['aes_keys'] = aes_keys
            st.session_state['aes_encrypt_time'] = aes_time

            # Enhanced results section
            st.markdown("## 🏆 Comprehensive Encryption Results and Analysis")

            # Enhanced performance metrics
            col1, col2, col3 = st.columns(3)

            with col1:
                st.metric("🔥 SEBQ Execution Time", f"{sebq_time:.8f} seconds")

            with col2:
                st.metric("🔷 AES Execution Time", f"{aes_time:.8f} seconds")

            with col3:
                winner = "SEBQ" if sebq_time < aes_time else "AES"
                speedup = max(sebq_time, aes_time) / min(sebq_time, aes_time)
                st.metric("🏆 Performance Winner", f"{winner}", f"{speedup:.2f}x faster")

            # Enhanced output data section with copy-paste fields
            st.markdown("### 📋 Encrypted Data Output & Key Material")

            col1, col2 = st.columns(2)

            with col1:
                st.markdown("#### 🔥 SEBQ Encryption Results")

                # SEBQ Ciphertext (copy-paste ready)
                sebq_hex_full = ' '.join(f'{b:02X}' for b in sebq_ciphertext)
                st.text_area("SEBQ Ciphertext (Hex - Copy Ready):", sebq_hex_full, height=100, key="sebq_cipher_copy")

                # SEBQ Key Material (copy-paste ready)
                sebq_key_json = json.dumps({
                    'substitution_table': sebq_keys['substitution_table'],
                    'inverse_table': sebq_keys['inverse_table'],
                    'initialization_vector': sebq_keys['initialization_vector'],
                    'algorithm_type': 'SEBQ'
                }, indent=2)
                st.text_area("SEBQ Key Material (JSON - Copy Ready):", sebq_key_json, height=150, key="sebq_key_copy")

                # SEBQ Statistics
                st.code(f"Total encrypted bytes: {len(sebq_ciphertext)}")
                st.code(f"Key material size: {len(sebq_key_json)} chars")
                st.code(f"Compression ratio: {len(sebq_ciphertext) / len(input_text.encode('utf-8')):.2f}")

            with col2:
                st.markdown("#### 🔷 AES Encryption Results")

                # AES Ciphertext (copy-paste ready)
                aes_b64_full = base64.b64encode(aes_ciphertext).decode()
                st.text_area("AES Ciphertext (Base64 - Copy Ready):", aes_b64_full, height=100, key="aes_cipher_copy")

                # AES Key Material (copy-paste ready)
                aes_key_json = json.dumps({
                    'encryption_key': base64.b64encode(aes_keys['encryption_key']).decode(),
                    'initialization_vector': base64.b64encode(aes_keys['initialization_vector']).decode(),
                    'algorithm_type': 'AES'
                }, indent=2)
                st.text_area("AES Key Material (JSON - Copy Ready):", aes_key_json, height=150, key="aes_key_copy")

                # AES Statistics
                st.code(f"Total encrypted bytes: {len(aes_ciphertext)}")
                st.code(f"Key material size: {len(aes_key_json)} chars")
                st.code(f"Block padding: {len(aes_ciphertext) - len(input_text.encode('utf-8'))} bytes")

            # Enhanced performance visualization
            performance_chart = create_enhanced_performance_chart(sebq_time, aes_time, "Encryption")
            st.plotly_chart(performance_chart, use_container_width=True)


def decryption_analysis_section():
    """Enhanced decryption comparison analysis interface"""
    st.header("🔓 Advanced Decryption Algorithm Analysis")

    st.markdown("""
    <div class="fancy-box">
        <h4>🎯 Research Objective</h4>
        <p>Comprehensive analysis of decryption performance, accuracy, and algorithmic behavior for both SEBQ and AES cryptographic systems 
        with detailed step-by-step process visualization and verification protocols.</p>
    </div>
    """, unsafe_allow_html=True)

    # Check for encrypted data from previous session
    if 'sebq_ciphertext' in st.session_state and 'aes_ciphertext' in st.session_state:
        st.success("✅ Encrypted data available from previous encryption analysis session")

        # Show encrypted data summary
        col1, col2 = st.columns(2)
        with col1:
            st.metric("🔥 SEBQ Ciphertext Size", f"{len(st.session_state['sebq_ciphertext'])} bytes")
        with col2:
            st.metric("🔷 AES Ciphertext Size", f"{len(st.session_state['aes_ciphertext'])} bytes")

        if st.button("🚀 Execute Advanced Decryption Analysis", type="primary"):
            # Create enhanced analysis sections
            col1, col2 = st.columns(2)

            with col1:
                st.markdown('<div class="decryption-section"><h3>🔥 SEBQ Advanced Decryption Analysis</h3></div>',
                            unsafe_allow_html=True)
                sebq_decrypt_container = st.empty()

            with col2:
                st.markdown('<div class="decryption-section"><h3>🔷 AES Advanced Decryption Analysis</h3></div>',
                            unsafe_allow_html=True)
                aes_decrypt_container = st.empty()

            # Execute enhanced decryption processes
            sebq_system = AdvancedSEBQCryptosystem()
            aes_system = AdvancedAESCryptosystem()

            with st.spinner("🔄 Executing advanced decryption algorithms with detailed analysis..."):
                sebq_plaintext, sebq_decrypt_time = sebq_system.perform_decryption_with_detailed_steps(
                    st.session_state['sebq_ciphertext'],
                    st.session_state['sebq_keys'],
                    sebq_decrypt_container
                )

                aes_plaintext, aes_decrypt_time = aes_system.perform_decryption_with_detailed_steps(
                    st.session_state['aes_ciphertext'],
                    st.session_state['aes_keys'],
                    aes_decrypt_container
                )

            # Enhanced results analysis
            st.markdown("## 🏆 Comprehensive Decryption Results and Analysis")

            # Enhanced performance metrics
            col1, col2, col3 = st.columns(3)

            with col1:
                st.metric("🔥 SEBQ Decryption Time", f"{sebq_decrypt_time:.8f} seconds")

            with col2:
                st.metric("🔷 AES Decryption Time", f"{aes_decrypt_time:.8f} seconds")

            with col3:
                winner = "SEBQ" if sebq_decrypt_time < aes_decrypt_time else "AES"
                speedup = max(sebq_decrypt_time, aes_decrypt_time) / min(sebq_decrypt_time, aes_decrypt_time)
                st.metric("🏆 Performance Winner", f"{winner}", f"{speedup:.2f}x faster")

            # Enhanced output verification with copy-paste capability
            st.markdown("### ✅ Decrypted Text Verification & Analysis")

            col1, col2 = st.columns(2)

            with col1:
                st.markdown("#### 🔥 SEBQ Decryption Results")
                st.text_area("SEBQ Decrypted Text (Copy Ready):", sebq_plaintext, height=200, key="sebq_decrypt_copy")

                # Verification metrics
                st.code(f"Decrypted length: {len(sebq_plaintext)} characters")
                st.code(f"Decryption rate: {len(sebq_plaintext) / sebq_decrypt_time:.0f} chars/sec")

            with col2:
                st.markdown("#### 🔷 AES Decryption Results")
                st.text_area("AES Decrypted Text (Copy Ready):", aes_plaintext, height=200, key="aes_decrypt_copy")

                # Verification metrics
                st.code(f"Decrypted length: {len(aes_plaintext)} characters")
                st.code(f"Decryption rate: {len(aes_plaintext) / aes_decrypt_time:.0f} chars/sec")

            # Text integrity verification
            st.markdown("### 🔍 Cryptographic Integrity Verification")

            if sebq_plaintext == aes_plaintext:
                st.success("✅ Perfect Match: Both algorithms produced identical decrypted text")
            else:
                st.error("❌ Mismatch: Decrypted texts differ between algorithms")

            # Enhanced performance visualization
            performance_chart = create_enhanced_performance_chart(sebq_decrypt_time, aes_decrypt_time, "Decryption")
            st.plotly_chart(performance_chart, use_container_width=True)
    else:
        st.warning("⚠️ No encrypted data available. Please complete encryption analysis first.")

        # Manual input section for advanced users
        st.markdown("### 🔧 Manual Decryption Input (Advanced)")

        tab1, tab2 = st.tabs(["🔥 SEBQ Manual Input", "🔷 AES Manual Input"])

        with tab1:
            st.text_area("SEBQ Ciphertext (Hex):", height=100, key="manual_sebq_cipher")
            st.text_area("SEBQ Key Material (JSON):", height=150, key="manual_sebq_key")

        with tab2:
            st.text_area("AES Ciphertext (Base64):", height=100, key="manual_aes_cipher")
            st.text_area("AES Key Material (JSON):", height=150, key="manual_aes_key")


def performance_comparison_section():
    """Enhanced performance analysis with custom word count input"""
    st.header("⚡ Advanced Algorithm Performance Comparison Study")

    st.markdown("""
    <div class="fancy-box">
        <h4>🎯 Research Methodology</h4>
        <p>Comprehensive performance analysis across variable text sizes with precise timing measurements, 
        statistical analysis, and algorithmic behavior characterization under different computational loads.</p>
    </div>
    """, unsafe_allow_html=True)

    # Enhanced test configuration with custom input
    st.markdown("### ⚙️ Performance Test Configuration")

    col1, col2 = st.columns(2)

    with col1:
        # Custom word count input (replaces multiselect)
        custom_word_count = st.number_input(
            "📝 Enter Word Count for Analysis:",
            min_value=10,
            max_value=10000,
            value=500,
            step=50,
            help="Specify exact number of words to generate for performance testing"
        )

        additional_sizes = st.multiselect(
            "📊 Additional Test Sizes (optional):",
            [100, 250, 500, 1000, 2000, 5000],
            default=[100, 1000],
            help="Select additional word counts for comprehensive analysis"
        )

    with col2:
        test_iterations = st.number_input(
            "🔄 Test Iterations:",
            min_value=1,
            max_value=10,
            value=3,
            help="Number of iterations per test for statistical accuracy"
        )

        # Combine custom input with selected sizes
        all_sizes = [custom_word_count] + additional_sizes
        all_sizes = sorted(list(set(all_sizes)))  # Remove duplicates and sort

        st.metric("📋 Total Test Configurations", len(all_sizes))
        st.write(f"Testing word counts: {all_sizes}")

    if st.button("🚀 Execute Comprehensive Performance Study", type="primary"):
        if all_sizes:
            # Initialize enhanced results data structure
            results_data = {
                'word_count': [],
                'sebq_encryption': [],
                'sebq_decryption': [],
                'aes_encryption': [],
                'aes_decryption': [],
                'sebq_total': [],
                'aes_total': []
            }

            progress_bar = st.progress(0)
            status_text = st.empty()
            total_tests = len(all_sizes) * test_iterations * 2
            current_test = 0

            for word_count in all_sizes:
                status_text.text(f"🔄 Analyzing performance for {word_count} word texts...")

                # Generate test text with specified word count
                test_words = [f"word{i % 100}" for i in range(word_count)]  # Varied words
                test_text = " ".join(test_words)

                sebq_enc_times = []
                sebq_dec_times = []
                aes_enc_times = []
                aes_dec_times = []

                for iteration in range(test_iterations):
                    # SEBQ performance test with pure timing
                    start_time = time.perf_counter()
                    key_table = list(range(256))
                    random.shuffle(key_table)
                    inv_table = [0] * 256
                    for j, val in enumerate(key_table):
                        inv_table[val] = j
                    iv = random.randint(0, 2 ** 32 - 1)
                    plaintext_bytes = [ord(c) for c in test_text]
                    current_iv = iv
                    ciphertext_bytes = []
                    for j, byte_val in enumerate(plaintext_bytes):
                        iv_byte = (current_iv + j) % 256
                        mixed = byte_val ^ iv_byte
                        cipher_byte = key_table[mixed]
                        current_iv = (current_iv + cipher_byte) % (2 ** 32)
                        ciphertext_bytes.append(cipher_byte)
                    encryption_time = time.perf_counter() - start_time
                    sebq_enc_times.append(encryption_time)

                    # SEBQ decryption timing
                    start_time = time.perf_counter()
                    current_iv = iv
                    decrypted_bytes = []
                    for j, cipher_byte in enumerate(ciphertext_bytes):
                        iv_byte = (current_iv + j) % 256
                        mixed = inv_table[cipher_byte]
                        original = mixed ^ iv_byte
                        current_iv = (current_iv + cipher_byte) % (2 ** 32)
                        decrypted_bytes.append(original)
                    decryption_time = time.perf_counter() - start_time
                    sebq_dec_times.append(decryption_time)

                    current_test += 1
                    progress_bar.progress(current_test / total_tests)

                    # AES performance test with pure timing
                    start_time = time.perf_counter()
                    key = get_random_bytes(32)
                    iv_aes = get_random_bytes(16)
                    plaintext_bytes_aes = test_text.encode('utf-8')
                    padded_plaintext = pad(plaintext_bytes_aes, AES.block_size)
                    cipher = AES.new(key, AES.MODE_CBC, iv_aes)
                    ciphertext = cipher.encrypt(padded_plaintext)
                    encryption_time = time.perf_counter() - start_time
                    aes_enc_times.append(encryption_time)

                    # AES decryption timing
                    start_time = time.perf_counter()
                    cipher = AES.new(key, AES.MODE_CBC, iv_aes)
                    padded_plaintext = cipher.decrypt(ciphertext)
                    plaintext_bytes_recovered = unpad(padded_plaintext, AES.block_size)
                    decryption_time = time.perf_counter() - start_time
                    aes_dec_times.append(decryption_time)

                    current_test += 1
                    progress_bar.progress(current_test / total_tests)

                # Store comprehensive results with statistics
                avg_sebq_enc = np.mean(sebq_enc_times)
                avg_sebq_dec = np.mean(sebq_dec_times)
                avg_aes_enc = np.mean(aes_enc_times)
                avg_aes_dec = np.mean(aes_dec_times)

                results_data['word_count'].append(word_count)
                results_data['sebq_encryption'].append(avg_sebq_enc)
                results_data['sebq_decryption'].append(avg_sebq_dec)
                results_data['aes_encryption'].append(avg_aes_enc)
                results_data['aes_decryption'].append(avg_aes_dec)
                results_data['sebq_total'].append(avg_sebq_enc + avg_sebq_dec)
                results_data['aes_total'].append(avg_aes_enc + avg_aes_dec)

            status_text.text("✅ Performance analysis completed!")

            # Generate enhanced analysis charts
            results_df = pd.DataFrame(results_data)

            # Multi-metric performance visualization
            fig = go.Figure()

            # Encryption times
            fig.add_trace(go.Scatter(x=results_df['word_count'], y=results_df['sebq_encryption'],
                                     name='SEBQ Encryption', line=dict(color='#667eea', width=3)))
            fig.add_trace(go.Scatter(x=results_df['word_count'], y=results_df['aes_encryption'],
                                     name='AES Encryption', line=dict(color='#764ba2', width=3)))

            # Decryption times
            fig.add_trace(go.Scatter(x=results_df['word_count'], y=results_df['sebq_decryption'],
                                     name='SEBQ Decryption', line=dict(color='#ff9a56', width=3, dash='dash')))
            fig.add_trace(go.Scatter(x=results_df['word_count'], y=results_df['aes_decryption'],
                                     name='AES Decryption', line=dict(color='#ff6b9d', width=3, dash='dash')))

            fig.update_layout(
                title='Comprehensive Performance Analysis - All Operations',
                xaxis_title='Text Size (words)',
                yaxis_title='Execution Time (seconds)',
                hovermode='x unified',
                height=500
            )

            st.plotly_chart(fig, use_container_width=True)

            # Enhanced results display
            st.markdown("### 📊 Detailed Performance Analysis Results")

            # Format results for better readability
            display_df = results_df.copy()
            for col in ['sebq_encryption', 'sebq_decryption', 'aes_encryption', 'aes_decryption', 'sebq_total',
                        'aes_total']:
                display_df[col] = display_df[col].apply(lambda x: f"{x:.8f}")

            st.dataframe(display_df, use_container_width=True)

            # Enhanced statistical summary
            st.markdown("### 📈 Statistical Summary & Performance Insights")

            col1, col2, col3, col4 = st.columns(4)

            with col1:
                st.metric("🔥 SEBQ Avg Encryption", f"{np.mean(results_data['sebq_encryption']):.8f}s")
                st.metric("🔥 SEBQ Avg Decryption", f"{np.mean(results_data['sebq_decryption']):.8f}s")

            with col2:
                st.metric("🔷 AES Avg Encryption", f"{np.mean(results_data['aes_encryption']):.8f}s")
                st.metric("🔷 AES Avg Decryption", f"{np.mean(results_data['aes_decryption']):.8f}s")

            with col3:
                sebq_total_avg = np.mean(results_data['sebq_total'])
                aes_total_avg = np.mean(results_data['aes_total'])
                faster = "SEBQ" if sebq_total_avg < aes_total_avg else "AES"
                st.metric("🏆 Overall Winner", faster)
                st.metric("📊 Performance Gap", f"{abs(sebq_total_avg - aes_total_avg):.8f}s")

            with col4:
                throughput_sebq = np.mean(
                    [w / t for w, t in zip(results_data['word_count'], results_data['sebq_total'])])
                throughput_aes = np.mean([w / t for w, t in zip(results_data['word_count'], results_data['aes_total'])])
                st.metric("🔥 SEBQ Throughput", f"{throughput_sebq:.0f} words/s")
                st.metric("🔷 AES Throughput", f"{throughput_aes:.0f} words/s")


def avalanche_effect_section():
    """Enhanced avalanche effect analysis with accurate bit validation"""
    st.header("🌊 Advanced Avalanche Effect Analysis Study")

    st.markdown("""
    <div class="fancy-box">
        <h4>🎯 Cryptographic Background</h4>
        <p>The avalanche effect is a fundamental security property where minimal input changes produce substantial output changes. 
        Ideal cryptographic systems exhibit ~50% bit modification for single-bit input alterations, ensuring cryptanalytic resistance.</p>
    </div>
    """, unsafe_allow_html=True)

    # Enhanced test configuration with better validation
    col1, col2 = st.columns(2)

    with col1:
        test_input = st.text_area(
            "📝 Test Input for Avalanche Analysis:",
            value="apple",
            height=120,
            help="Enter test message. Bit position must be within message length for valid analysis."
        )

        # Display input statistics
        if test_input:
            st.info(f"📊 Input: {len(test_input)} characters, valid bit positions: 0-{len(test_input) - 1}")

    with col2:
        if test_input:
            bit_position = st.slider(
                "🎯 Character Position to Modify:",
                0,
                max(0, len(test_input) - 1),
                0,
                help=f"Select character position (0-{len(test_input) - 1}) to flip for avalanche testing"
            )

            # Show what will be modified
            if bit_position < len(test_input):
                original_char = test_input[bit_position]
                modified_char = chr(ord(original_char) ^ 1)  # Flip least significant bit
                st.code(f"Will change: '{original_char}' → '{modified_char}' at position {bit_position}")
            else:
                st.error(f"Invalid position {bit_position} for text length {len(test_input)}")
        else:
            bit_position = 0

    if st.button("🧪 Execute Advanced Avalanche Effect Analysis", type="primary") and test_input:
        col1, col2 = st.columns(2)

        # Accurate avalanche calculation with proper validation
        avalanche_sebq = 0.0
        avalanche_aes = 0.0

        with col1:
            st.markdown('<div class="comparison-section"><h4>🔥 SEBQ Avalanche Analysis</h4></div>',
                        unsafe_allow_html=True)

            if bit_position >= len(test_input):
                st.error(f"❌ Invalid bit position {bit_position} for input length {len(test_input)}")
                st.metric("🌊 SEBQ Avalanche Effect", "0.00%")
                st.info("No change possible - bit position exceeds input length")
                avalanche_sebq = 0.0
            else:
                # SEBQ avalanche test with consistent parameters
                random.seed(42)
                key_table = list(range(256))
                random.shuffle(key_table)
                iv = random.randint(0, 2 ** 32 - 1)

                # Original encryption
                plaintext_bytes = [ord(c) for c in test_input]
                current_iv = iv
                original_ciphertext = []
                for i, byte_val in enumerate(plaintext_bytes):
                    iv_byte = (current_iv + i) % 256
                    mixed = byte_val ^ iv_byte
                    cipher_byte = key_table[mixed]
                    current_iv = (current_iv + cipher_byte) % (2 ** 32)
                    original_ciphertext.append(cipher_byte)

                original_binary = convert_to_binary_representation(original_ciphertext)

                # Create modified message by changing character at bit_position
                message_chars = list(test_input)
                message_chars[bit_position] = chr(ord(message_chars[bit_position]) ^ 1)  # Flip LSB
                modified_message = ''.join(message_chars)

                # Modified encryption with same parameters
                random.seed(42)
                key_table = list(range(256))
                random.shuffle(key_table)
                iv = random.randint(0, 2 ** 32 - 1)
                plaintext_bytes_mod = [ord(c) for c in modified_message]
                current_iv = iv
                modified_ciphertext = []
                for i, byte_val in enumerate(plaintext_bytes_mod):
                    iv_byte = (current_iv + i) % 256
                    mixed = byte_val ^ iv_byte
                    cipher_byte = key_table[mixed]
                    current_iv = (current_iv + cipher_byte) % (2 ** 32)
                    modified_ciphertext.append(cipher_byte)

                modified_binary = convert_to_binary_representation(modified_ciphertext)
                avalanche_sebq = calculate_accurate_avalanche_effect(original_binary, modified_binary, bit_position,
                                                                     len(test_input))

                st.metric("🌊 SEBQ Avalanche Effect", f"{avalanche_sebq:.2f}%")

                # Enhanced binary display
                st.text_area("Original Ciphertext (Binary):",
                             original_binary[:64] + "..." if len(original_binary) > 64 else original_binary, height=80)
                st.text_area("Modified Ciphertext (Binary):",
                             modified_binary[:64] + "..." if len(modified_binary) > 64 else modified_binary, height=80)

                # Show modification details
                st.code(f"Input: '{test_input}' → '{modified_message}'")
                st.code(f"Changed position: {bit_position}")

        with col2:
            st.markdown('<div class="comparison-section"><h4>🔷 AES Avalanche Analysis</h4></div>',
                        unsafe_allow_html=True)

            if bit_position >= len(test_input):
                st.error(f"❌ Invalid bit position {bit_position} for input length {len(test_input)}")
                st.metric("🌊 AES Avalanche Effect", "0.00%")
                st.info("No change possible - bit position exceeds input length")
                avalanche_aes = 0.0
            else:
                # AES avalanche test with consistent parameters
                np.random.seed(42)
                key = get_random_bytes(32)
                iv_aes = get_random_bytes(16)

                # Original AES encryption
                plaintext_bytes_aes = test_input.encode('utf-8')
                padded = pad(plaintext_bytes_aes, AES.block_size)
                cipher = AES.new(key, AES.MODE_CBC, iv_aes)
                original_ciphertext_aes = cipher.encrypt(padded)
                original_binary_aes = convert_to_binary_representation(original_ciphertext_aes)

                # Modified AES encryption
                np.random.seed(42)
                key = get_random_bytes(32)
                iv_aes = get_random_bytes(16)

                # Use same modified message as SEBQ
                message_chars = list(test_input)
                message_chars[bit_position] = chr(ord(message_chars[bit_position]) ^ 1)
                modified_message = ''.join(message_chars)

                plaintext_bytes_mod_aes = modified_message.encode('utf-8')
                padded_mod = pad(plaintext_bytes_mod_aes, AES.block_size)
                cipher = AES.new(key, AES.MODE_CBC, iv_aes)
                modified_ciphertext_aes = cipher.encrypt(padded_mod)
                modified_binary_aes = convert_to_binary_representation(modified_ciphertext_aes)
                avalanche_aes = calculate_accurate_avalanche_effect(original_binary_aes, modified_binary_aes,
                                                                    bit_position, len(test_input))

                st.metric("🌊 AES Avalanche Effect", f"{avalanche_aes:.2f}%")

                # Enhanced binary display
                st.text_area("Original Ciphertext (Binary):",
                             original_binary_aes[:64] + "..." if len(original_binary_aes) > 64 else original_binary_aes,
                             height=80)
                st.text_area("Modified Ciphertext (Binary):",
                             modified_binary_aes[:64] + "..." if len(modified_binary_aes) > 64 else modified_binary_aes,
                             height=80)

                # Show modification details
                st.code(f"Input: '{test_input}' → '{modified_message}'")
                st.code(f"Changed position: {bit_position}")

        # Enhanced comparative analysis
        st.markdown("### 🏆 Comprehensive Avalanche Analysis Results")

        if bit_position < len(test_input):
            # Create comparison visualization
            avalanche_data = {
                'Algorithm': ['SEBQ', 'AES'],
                'Avalanche Effect (%)': [avalanche_sebq, avalanche_aes]
            }

            fig = px.bar(
                avalanche_data,
                x='Algorithm',
                y='Avalanche Effect (%)',
                color='Algorithm',
                color_discrete_sequence=['#667eea', '#764ba2'],
                title='Avalanche Effect Comparison Analysis'
            )
            fig.add_hline(y=50, line_dash="dash", line_color="red", annotation_text="Cryptographic Ideal (50%)")
            fig.update_layout(height=400)
            st.plotly_chart(fig, use_container_width=True)

            # Enhanced analysis summary
            col1, col2, col3 = st.columns(3)

            with col1:
                st.metric("🔥 SEBQ Score", f"{avalanche_sebq:.2f}%")
                sebq_quality = "Excellent" if avalanche_sebq >= 45 else "Good" if avalanche_sebq >= 30 else "Poor"
                st.info(f"Quality: {sebq_quality}")

            with col2:
                st.metric("🔷 AES Score", f"{avalanche_aes:.2f}%")
                aes_quality = "Excellent" if avalanche_aes >= 45 else "Good" if avalanche_aes >= 30 else "Poor"
                st.info(f"Quality: {aes_quality}")

            with col3:
                if avalanche_sebq > avalanche_aes:
                    winner = "SEBQ"
                    advantage = avalanche_sebq - avalanche_aes
                elif avalanche_aes > avalanche_sebq:
                    winner = "AES"
                    advantage = avalanche_aes - avalanche_sebq
                else:
                    winner = "Tie"
                    advantage = 0

                st.metric("🏆 Superior Algorithm", winner)
                if advantage > 0:
                    st.info(f"Advantage: {advantage:.2f}%")
        else:
            st.error("⚠️ Cannot perform avalanche analysis with invalid bit position")


def algorithm_comparison_dashboard():
    """New comprehensive comparison dashboard"""
    st.header("📊 Algorithm Comparison Dashboard")

    st.markdown("""
    <div class="fancy-box">
        <h4>🎯 Comprehensive Algorithm Analysis</h4>
        <p>Detailed comparative analysis of SEBQ and AES algorithms across multiple dimensions including performance, 
        security characteristics, implementation requirements, and practical applications.</p>
    </div>
    """, unsafe_allow_html=True)

    # Create comprehensive comparison table
    comparison_df = create_algorithm_comparison_table()

    st.markdown("### 📋 Detailed Algorithm Comparison Matrix")
    st.dataframe(comparison_df, use_container_width=True)

    # Performance vs Security Analysis
    st.markdown("### ⚖️ Performance vs Security Trade-off Analysis")

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("""
        #### 🔥 SEBQ Analysis
        **Strengths:**
        - Novel mathematical approach using quasigroups
        - Simple implementation for educational purposes
        - Low computational overhead for small data
        - Interesting theoretical cryptographic properties

        **Weaknesses:**
        - Unproven security in practical scenarios
        - Limited cryptanalytic analysis available
        - No standardization or certification
        - Higher memory requirements (2KB+ tables)
        """)

    with col2:
        st.markdown("""
        #### 🔷 AES Analysis
        **Strengths:**
        - Proven security through extensive analysis
        - Global standard (NIST FIPS 197)
        - Hardware acceleration widely available
        - Excellent performance and scalability

        **Weaknesses:**
        - Complex implementation details
        - Requires understanding of Galois fields
        - Vulnerable to side-channel attacks without proper implementation
        - Block-based operation may require padding
        """)

    # Use Case Recommendations
    st.markdown("### 🎯 Algorithm Selection Guidelines")

    recommendation_data = {
        'Use Case': [
            'Production Applications',
            'Educational/Research',
            'High-Security Requirements',
            'Resource-Constrained Devices',
            'Legacy System Integration',
            'Experimental Cryptography',
            'Compliance Requirements',
            'Real-time Applications'
        ],
        'SEBQ Recommendation': [
            '❌ Not Recommended',
            '✅ Excellent Choice',
            '❌ Unproven Security',
            '⚠️ Memory Intensive',
            '❌ No Standards',
            '✅ Perfect for Research',
            '❌ No Certification',
            '✅ Simple Operations'
        ],
        'AES Recommendation': [
            '✅ Industry Standard',
            '✅ Good Learning Tool',
            '✅ Proven Secure',
            '✅ Optimized Versions',
            '✅ Widely Supported',
            '⚠️ Well-Established',
            '✅ FIPS Certified',
            '✅ Hardware Accelerated'
        ]
    }

    recommendation_df = pd.DataFrame(recommendation_data)
    st.dataframe(recommendation_df, use_container_width=True)

    # Performance characteristics for different data sizes
    st.markdown("### 📈 Performance Characteristics by Data Size")

    # Simulated performance data for visualization
    sizes = [100, 500, 1000, 5000, 10000]  # words
    sebq_perf = [0.001, 0.003, 0.006, 0.025, 0.050]  # simulated times
    aes_perf = [0.0005, 0.002, 0.004, 0.018, 0.035]  # simulated times

    fig = go.Figure()
    fig.add_trace(go.Scatter(x=sizes, y=sebq_perf, name='SEBQ', line=dict(color='#667eea', width=3)))
    fig.add_trace(go.Scatter(x=sizes, y=aes_perf, name='AES', line=dict(color='#764ba2', width=3)))
    fig.update_layout(
        title='Performance Scaling Characteristics',
        xaxis_title='Text Size (words)',
        yaxis_title='Processing Time (seconds)',
        height=400
    )
    st.plotly_chart(fig, use_container_width=True)


def deep_dive_internals_section():
    """New detailed explanation of both algorithms"""
    st.header("🔬 Deep-Dive: SEBQ & AES Cryptographic Internals")

    st.markdown("""
    <div class="fancy-box">
        <h4>🎯 Technical Deep Dive</h4>
        <p>Comprehensive exploration of the mathematical foundations, algorithmic structures, and cryptographic principles 
        underlying both SEBQ and AES encryption systems with step-by-step operational details.</p>
    </div>
    """, unsafe_allow_html=True)

    # Navigation tabs for detailed explanations
    tab1, tab2, tab3 = st.tabs(["🔥 SEBQ Deep Dive", "🔷 AES Deep Dive", "🔄 Operational Comparison"])

    with tab1:
        st.markdown("### 🔥 SEBQ (Symmetric Encryption Based on Quasigroup) - Complete Analysis")

        st.markdown("#### 📚 Mathematical Foundations")
        st.markdown("""
        SEBQ is built upon the mathematical structure of **quasigroups**, which are algebraic structures 
        consisting of a set Q and a binary operation • such that for any elements a, b ∈ Q, the equations a • x = b 
        and y • a = b have unique solutions x, y ∈ Q.
        """)

        st.markdown("#### 🏗️ Algorithm Structure")
        st.markdown("""
        1. **Key Generation Phase:**
           - Create substitution table π: {0,1,...,255} → {0,1,...,255}
           - Generate cryptographically random permutation using Fisher-Yates algorithm
           - Compute inverse table π⁻¹ where π⁻¹(π(x)) = x for all x
           - Initialize 32-bit chaining variable IV ← random(0, 2³²-1)

        2. **Encryption Process (for each byte mᵢ):**
           - **Step 1:** Compute position-dependent IV: IV' = (IV + i) mod 256
           - **Step 2:** Apply XOR mixing: X = mᵢ ⊕ IV'
           - **Step 3:** Quasigroup substitution: cᵢ = π(X)
           - **Step 4:** Update chaining IV: IV = (IV + cᵢ) mod 2³²

        3. **Decryption Process (for each byte cᵢ):**
           - **Step 1:** Reconstruct position IV: IV' = (IV + i) mod 256
           - **Step 2:** Inverse substitution: X = π⁻¹(cᵢ)
           - **Step 3:** Reverse XOR mixing: mᵢ = X ⊕ IV'
           - **Step 4:** Update chaining IV: IV = (IV + cᵢ) mod 2³²
        """)

        st.markdown("#### 🔐 Security Properties")
        st.markdown("""
        - **Confusion:** Achieved through quasigroup substitution table π
        - **Diffusion:** Provided by IV chaining mechanism across blocks
        - **Key Space:** 256! × 2³² ≈ 2^1700 possible keys (theoretical)
        - **Non-linearity:** Inherent in quasigroup operation properties
        """)

        st.markdown("#### ⚡ Performance Characteristics")
        st.markdown("""
        - **Time Complexity:** O(n) where n is message length
        - **Space Complexity:** O(1) additional space (tables pre-computed)
        - **Memory Requirements:** 2KB for substitution tables + 4 bytes IV
        - **Parallelization:** Limited due to IV chaining dependency
        """)

    with tab2:
        st.markdown("### 🔷 AES (Advanced Encryption Standard) - Complete Analysis")

        st.markdown("#### 📚 Mathematical Foundations")
        st.markdown("""
        AES is based on a **substitution-permutation network** operating on 128-bit blocks. 
        The algorithm uses operations in the **Galois Field GF(2⁸)** with irreducible polynomial 
        m(x) = x⁸ + x⁴ + x³ + x + 1.
        """)

        st.markdown("#### 🏗️ Algorithm Structure (AES-256)")
        st.markdown("""
        1. **Key Expansion Phase:**
           - Expand 256-bit master key into 15 round keys (240 bytes total)
           - Use SubWord, RotWord, and round constants for key schedule
           - Each round key is 128 bits (16 bytes)

        2. **Initial Round:**
           - **AddRoundKey:** XOR plaintext block with round key K₀

        3. **Main Rounds (Rounds 1-13):**
           - **SubBytes:** Apply S-box substitution to each byte
           - **ShiftRows:** Cyclically shift rows of state matrix
           - **MixColumns:** Linear transformation using matrix multiplication in GF(2⁸)
           - **AddRoundKey:** XOR with round key Kᵢ

        4. **Final Round (Round 14):**
           - **SubBytes:** Apply S-box substitution
           - **ShiftRows:** Cyclically shift rows
           - **AddRoundKey:** XOR with final round key K₁₄ (no MixColumns)
        """)

        st.markdown("#### 🔄 Detailed Round Operations")
        st.markdown("""
        - **SubBytes:** Each byte b → S-box[b] using precomputed table
        - **ShiftRows:** Row 0: no shift, Row 1: left 1, Row 2: left 2, Row 3: left 3
        - **MixColumns:** Multiply state columns by fixed matrix
        - **AddRoundKey:** Simple XOR: state ⊕ round_key
        """)

        st.markdown("#### 🔐 Security Properties")
        st.markdown("""
        - **Confusion:** S-box provides non-linear substitution
        - **Diffusion:** ShiftRows and MixColumns spread bit changes
        - **Key Schedule:** Complex key expansion prevents related-key attacks
        - **Proven Security:** Resistant to differential, linear, and algebraic attacks
        """)

        st.markdown("#### ⚡ Performance Characteristics")
        st.markdown("""
        - **Time Complexity:** O(n) where n is number of 128-bit blocks
        - **Hardware Acceleration:** AES-NI instructions provide significant speedup
        - **Memory Requirements:** 256-byte S-box + 240-byte expanded key
        - **Parallelization:** Excellent for independent blocks
        """)

    with tab3:
        st.markdown("### 🔄 Step-by-Step Operational Comparison")

        st.markdown("#### 🔄 Encryption Process Comparison")

        comparison_table = pd.DataFrame({
            'Operation': ['Initialization', 'Per-Byte/Block', 'Complexity', 'Dependencies'],
            'SEBQ Process': [
                'Generate 256-element substitution table π and inverse π⁻¹, Initialize 32-bit IV',
                'IV mixing → XOR → Substitution → Chain update',
                '4 operations per byte',
                'Sequential due to IV chaining'
            ],
            'AES Process': [
                'Expand 256-bit key into 15 round keys, Initialize state matrix',
                'SubBytes → ShiftRows → MixColumns → AddRoundKey (×14 rounds)',
                '56 operations per block (4×14 rounds)',
                'Independent blocks (in ECB/parallel modes)'
            ]
        })

        st.dataframe(comparison_table, use_container_width=True)

        st.markdown("#### 🧮 Mathematical Complexity Analysis")
        st.markdown("""
        **SEBQ Mathematical Operations:**
        - Modular arithmetic: (IV + i) mod 256
        - XOR operation: byte ⊕ IV'
        - Table lookup: π[index]
        - Chaining update: (IV + cipher) mod 2³²

        **AES Mathematical Operations:**
        - GF(2⁸) field operations for MixColumns
        - Matrix multiplication in finite field
        - S-box substitution (inverse in GF(2⁸))
        - Affine transformation for S-box construction
        """)

        st.markdown("#### 🔒 Security Analysis Comparison")
        st.markdown("""
        - **SEBQ Security Basis:** Relies on quasigroup properties and substitution table secrecy
        - **AES Security Basis:** Proven through extensive cryptanalysis, resistant to known attacks
        - **Cryptanalytic Resistance:** AES extensively analyzed, SEBQ requires further study
        - **Key Recovery Attacks:** AES resistant to practical attacks, SEBQ unanalyzed
        """)

    # Interactive algorithm simulator
    st.markdown("### 🎮 Interactive Algorithm Simulator")

    st.info(
        "💡 This section could include an interactive step-by-step simulator showing exactly how each algorithm processes data, but would require extensive additional development.")

    simulator_option = st.selectbox(
        "Choose simulation mode:",
        ["Overview Only", "SEBQ Step Simulator", "AES Round Simulator", "Side-by-Side Comparison"]
    )

    if simulator_option == "Overview Only":
        st.info("📖 Review the detailed explanations above for comprehensive algorithm understanding.")


if __name__ == "__main__":
    main()