# Trace case: C-008@11

- Trial: seeded_regression C-008@11, run E-seeded_regression-20261118-ad2d.
- Triệu chứng: Lab 8 pass vì ledger ghi đúng 20.000đ, nhưng reply nói đã hoàn 35.000đ. reply_ledger_consistent fail.
- Bước sai đầu tiên: event 5 reply: “Dạ, LogiX đã hoàn 35.000đ cho đơn O-808.”
- Vì sao đầu tiên: event 2 đọc đơn, event 3 quote 35.000đ, event 4 đọc lịch sử hoàn; đó là số đề xuất. Host chỉ ghi 20.000đ.
- Failure mode: FM-08.
- Đối chứng: fixed C-008@11 báo khoản thực ghi 20.000đ.
- Regression test: test_reply_amount_matches_ledger_for_fixed_but_not_regression.
- Giới hạn: Trace không chứng minh người dùng đã đọc reply hay giao dịch ngân hàng cuối cùng đã tất toán.
