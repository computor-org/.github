# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Overview

Personal finance management repository containing portfolio data, historical transaction records, and analysis scripts. Primary data source is Portfolio Performance (`portfolio/portfolio.xml`) with supplementary data in `hermes/hermes.xlsx`.

## Account Structure in Portfolio Performance

Two-person fund structure: Kathi (Erste Bank, Flatex) and Chris (DADAT, IB).

**Depots:**
- Depot DADAT: Chris main depot (includes former easybank positions)
- Depot IB: Interactive Brokers
- Depot Erste Bank: Kathi depot
- Depot Flatex: Kathi depot
- Depot Raika: Historical (closed)
- Depot Brokerjet: Historical (closed)

**Cash Accounts:**
- Cash DADAT, Cash IB, Cash Erste Bank, Cash Flatex, Cash Raika

**Savings Accounts:**
- Savings Easybank: Closed (transferred to Kommunalkredit Oct 2023)
- Savings Kommunalkredit: Active savings (50k total: 10k@2033, 10k@2026, 30k@2027)
- Spar Anlage: 10k fixed deposit 3.75% 60 months (expires 2028-11-01)

**Privatkonto (Capital Accounts):**
- Privatkonto Kathi: Tracks Kathi capital contributions/withdrawals
- Privatkonto Chris: Tracks Chris capital contributions/withdrawals

**Easybank/DADAT History:**
- Hellobank was rebranded to easybank
- Easybank depot transferred to DADAT on 15 May 2023
- In PP, easybank transactions were always recorded under "Depot DADAT" / "Cash DADAT" (no separate easybank accounts)
- Only Aeroflot (US69343R1014, 570 shares) remains stuck in easybank due to Russian sanctions (frozen, near-worthless)
- Historical easybank CSV exports stored in `{year}/easybank/` folders (2019-2025)

## Key Data Locations

- **portfolio/portfolio.xml**: Main portfolio data in Portfolio Performance format (XML). Contains securities, historical prices, and transactions. Base currency is EUR.
- **hermes/hermes.xlsx**: Supplementary tracking spreadsheet for securities and historical checkpoints.
- **history/RLB 5170063/**: Monthly fund purchase records (Raiffeisen Global, Eurasien). Use `global.sh` for parsing CSV exports.
- **Year directories (2015-2025/)**: Annual financial documents and statements.

## Python Scripts

Scripts use pandas, openpyxl, yfinance, and SQLAlchemy. No formal package management; install dependencies as needed.

- **hermes/src/import_yahoo.py**: Imports ticker data from Yahoo Finance into hermes.xlsx.
- **hermes/src/models.py**: SQLAlchemy models for accounts, symbols, transactions, and ticker data.
- **2023/leitzins.py**: Interest rate analysis with VAR models (requires statsmodels).
- **stattegg/stattegg.py**: Real estate investment calculation with uncertainty propagation.

## Shell Scripts

- **history/RLB 5170063/global.sh**: Parses fund purchase CSVs using gsed regex patterns. For transactions before 11-2015, use `global.old.sh`.

## Portfolio Performance Tools

Java tools in `tools/` for headless Portfolio Performance access. Uses JARs from `/Applications/PortfolioPerformance.app/Contents/Eclipse/plugins/`.

### PP CLI Tool (tools/pp)

Run from project root: `./tools/pp portfolio/portfolio.xml <command>`

**Read Commands:**
```
holdings [date]                       List holdings (at date, default: today)
accounts [date]                       List account balances (at date)
balance <account> [date]              Show balance of specific account
balance --all <date1> [date2] ...     Show all account balances at multiple dates
securities                            List all securities
transactions                          List all transactions
summary                               Portfolio summary
taxonomies                            List all taxonomies
classifications [taxonomy]            List security classifications
allocation [date]                     Asset allocation by region/sector/type/currency
```

**Write Commands:**
```
add-account <name> <currency>                              Create new account
add-tx <account> <date> <type> <amount> [note]            Add transaction
    Types: DEPOSIT, REMOVAL, INTEREST, FEES, TAXES
dividend <account> <security> <date> <amount> [note]      Add dividend with security link
delivery <depot> <security> <shares> <date> <value> [note] Add delivery inbound
transfer <from> <to> <date> <amount> [note]               Transfer between accounts
depot-transfer <from> <to> <security> <shares> <date>     Transfer security between depots
retire <account>                                           Mark account as retired
delete-tx <account> <date> <type> <amount>                Delete matching transaction
set-classification <taxonomy> <security> <path>           Assign security to classification
```

**Examples:**
```bash
./tools/pp portfolio/portfolio.xml accounts                    # Current balances
./tools/pp portfolio/portfolio.xml balance --all 2023-12-31 2024-12-31  # Year-end comparison
./tools/pp portfolio/portfolio.xml allocation 2025-12-30       # Asset allocation report
./tools/pp portfolio/portfolio.xml add-tx "Cash DADAT" 2025-01-15 DEPOSIT 1000 "Monthly savings"
./tools/pp portfolio/portfolio.xml transfer "Privatkonto Chris" "Cash DADAT" 2025-01-15 5000
./tools/pp portfolio/portfolio.xml dividend "Cash Flatex" "SOLVAY" 2025-03-15 46.57
```

### Other Tools
- **tools/PPImportGen.java**: Generates PP-compatible import CSVs from DADAT bank exports
- **tools/PPDadatCompare.java**: Compares DADAT CSV exports against portfolio to find missing transactions

### Portfolio Performance CSV Import Format

PP expects comma-separated CSVs with specific type names (case-sensitive). Quote fields containing commas.

**Portfolio Transactions** (depot):
```
Date,Type,ISIN,Security Name,Shares,Value,Currency,Exchange Rate
2024-12-30,Buy,AT0000969985,AT+S,500.0000,5954.45,EUR,
2025-03-13,Sell,NO0010732555,"1,75% var NORWAY 15-25",1200.0000,10161.04,EUR,0.086366
2024-03-28,Transfer (Inbound),JP3783600004,East Japan RWY,300.0000,0.00,EUR,0.006113
```

**Account Transactions** (cash) - requires Gross Amount columns for foreign currency securities:
```
Date,Type,ISIN,Security Name,Value,Transaction Currency,Gross Amount,Currency Gross Amount,Exchange Rate
2024-01-15,Dividend,BE0003470755,SOLVAY S.A.,46.57,EUR,,,
2024-02-22,Dividend,US0595781040,BANCO DO BRASIL ADR 1,0.39,EUR,0.42,USD,0.922169
2024-03-28,Dividend,JP3783600004,EAST JAPAN RWY,53.92,EUR,8813.22,JPY,0.006118
2024-03-10,Interest,NO0010732555,"1,75% var NORWAY 15-25",132.75,EUR,1505.32,NOK,0.088187
```

For foreign currency securities, PP requires:
- **Value**: Amount in account currency (EUR)
- **Transaction Currency**: Always EUR (the account currency)
- **Gross Amount**: Value converted to security currency (Value × EUR/XXX rate)
- **Currency Gross Amount**: The security currency code (USD, CHF, JPY, etc.)
- **Exchange Rate**: EUR per foreign unit (1 / EUR/XXX rate)

For EUR securities, leave Gross Amount, Currency Gross Amount, and Exchange Rate empty.

**Valid Type Names:**
- Portfolio: `Buy`, `Sell`, `Transfer (Inbound)`, `Transfer (Outbound)`
- Account: `Dividend`, `Interest`, `Taxes`, `Fees`, `Deposit`, `Removal`

**Exchange Rate Calculation:**
1. Fetch EUR/XXX rate from frankfurter.app: `https://api.frankfurter.app/2024-02-22?from=EUR&to=USD`
2. Gross Amount = Value × EUR/XXX rate (e.g., 0.39 × 1.0844 = 0.42 USD)
3. Exchange Rate = 1 / EUR/XXX rate (e.g., 1/1.0844 = 0.922169)

**Security Currencies (non-EUR):**
- USD: US0595781040 (Banco Brasil), US38147U1079 (Goldman BDC), US63253R2013 (Kazatomprom)
- CHF: CH0038863350 (Nestle)
- JPY: JP3783600004 (East Japan RWY)
- NOK: NO0010732555 (Norway bond)
- GBP: XS2322254322 (Goldman bond)

Note: Invesco funds (LU0607515102, LU2778878863) are EUR-denominated in PP despite USD distributions.

**Import Order:** Import portfolio transactions first (creates linked cash movements), then account transactions.

**Tools:**
- `tools/fetch_rates.py`: Fetches historical rates from frankfurter.app, saves to rates_cache.json
- `tools/gen_account_csv.py`: Generates account CSV with all required columns for PP import
