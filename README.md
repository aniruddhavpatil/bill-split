# Bill Split
A simple Python program to help you split bills.

To run, use `python3 bill_split.py <input_file_path>`

Input File Format
```
<name_1> <name_2> ... <name_n>
<item_1> <name_1_share> <name_2_share> ... <name_n_share> <cost>
<item_2> <name_1_share> <name_2_share> ... <name_n_share> <cost>
.
.
.
<item_m> <name_1_share> <name_2_share> ... <name_n_share> <cost>
<total_cost>
```

`<name_x_share>` can be integers or decimals

Output File Format
```
<name_1> items:
(<item_1>, <name_1_share>, <name_1_cost>)
(<item_2>, <name_1_share>, <name_1_cost>)
.
.
.
(<item_n>, <name_1_share>, <name_1_cost>)
<name_1> subtotal
<name_1> tax/discount
<name_1> total

<name_2> items:
(<item_1>, <name_2_share>, <name_2_cost>)
(<item_2>, <name_2_share>, <name_2_cost>)
.
.
.
(<item_n>, <name_2_share>, <name_2_cost>)
<name_2> subtotal
<name_2> tax/discount
<name_2> total

.
.
.

<name_n> items:
(<item_1>, <name_n_share>, <name_n_cost>)
(<item_2>, <name_n_share>, <name_n_cost>)
.
.
.
(<item_n>, <name_n_share>, <name_n_cost>)
<name_n> subtotal
<name_n> tax/discount
<name_n> total

final_total
```

The file `test_input.txt` contains a test input.
