target_sum = 2020;
load("-ascii","input.txt");
n = rows(input);
solution_i = [];
solution_j = [];
for i = 1:n
        for j = i:n
                if( input(i) + input(j) == target_sum )
                        solution_i = [solution_i, i];
                        solution_j = [solution_j, j];
                        solution = input(i)*input(j);
                endif
        endfor
endfor
