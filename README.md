# CS 475/575 – Project #4: SIMD Array Multiplication and Reduction

**Author:** Blayton Vidrine
**Course:** CS 475/575 – High-Performance Computing
**Project:** Vectorized Array Multiplication and Multiplication/Reduction using SSE
**Platform:** Tested on `flip.engr.oregonstate.edu`

---

## 📋 Overview

This project benchmarks the performance of standard C++ array multiplication and reduction operations against their SIMD-enhanced versions using SSE instructions. Speedup is calculated and graphed for various array sizes ranging from 1K to 8M.

---

## 📁 Files

* `all04.cpp` – Main program performing SIMD and non-SIMD benchmarks.
* `run_all.sh` – Automation script for compiling and running tests across multiple array sizes.
* `plot_speedup.py` – Python script to parse `results.txt` and generate a speedup graph.
* `results.txt` – Raw benchmark output from `run_all.sh`.
* `speedup_plot.png` – Final graph comparing SIMD and non-SIMD performance.

---

## 🚀 How to Run

### 1. Clone the Repository

```bash
git clone https://github.com/BlaytonV/CS475-Project-4.git
cd CS475-Project-4
```

### 2. Run Benchmarks on flip

```bash
chmod +x run_all.sh
./run_all.sh
```

This will:

* Compile `all04.cpp` for each array size.
* Run benchmarks.
* Append results to `results.txt`.

### 3. Generate the Graph (Optional – on local machine or flip with virtualenv)

```bash
python3 plot_speedup.py
```

Output will be saved as `speedup_plot.png`.

---

## 📊 Result Summary

* SIMD consistently outperforms non-SIMD while array sizes fit within CPU cache.
* Performance drops at large sizes due to cache and memory bandwidth constraints.
* Full analysis and table included in `Vidrine_Blayton_Project4_Commentary.docx`.

---

## ⚠️ Notes

* Do **not** use optimization flags (`-O2`, `-O3`) with `all04.cpp`, as they can interfere with raw SSE assembly.
* Results may vary depending on hardware and memory/cache architecture.
