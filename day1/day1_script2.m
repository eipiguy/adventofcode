target_sum = 2020;

load("-ascii","input.txt");
n = rows(input);

solution_i = [];
solution_j = [];
solution_k = [];

for i = 1:n
        for j = i:n
                for k = j:n
                        if( input(i) + input(j) + input(k) == target_sum )
                                solution_i = [solution_i, i];
                                solution_j = [solution_j, j];
                                solution_k = [solution_k, k];
                                solution = input(i)*input(j)*input(k);
                        endif
                endfor
        endfor
endfor
