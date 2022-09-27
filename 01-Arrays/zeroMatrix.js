// Write an algorithm such that if an element in an MxN matrix is 0, its entire row and column are set to 0.
// Time complexity: ??
// Space complexity: O(N*M), it can be reduced to O(N)

function markZeros(matrix){
    var ceroCoordenates = new Array();

    for(let i = 0; i < matrix.length; i++){
        for(let j = 0; j < matrix[0].length; j++){
            if(matrix[i][j] == 0){
                ceroCoordenates.push([i,j]);
            }
        }
    }

    // Z zeros * (R rows + C columns) = O(Z(R+C))
    for(let i = 0; i < ceroCoordenates.length; i++){
        const row = ceroCoordenates[i][0];
        const col = ceroCoordenates[i][1];

        console.log(ceroCoordenates[i])

        // Zeros on col
        for(let j = 0; j < matrix[0].length; j++){
            matrix[row][j] = 0;
        }

        // Zeros on row
        for(let k = 0; k < matrix.length; k++){
            matrix[k][col] = 0;
        }
    }

    console.log(ceroCoordenates);
    return matrix;
}

const matrix1 = [
    [1, 1, 1, 1, 1],
    [0, 1, 1, 1, 1],
    [1, 1, 0, 1, 1],
    [1, 1, 1, 1, 0],
    [1, 1, 1, 1, 1],
];

const matrix2 = [
    [1, 2, 3, 0],
    [4, 0, 5, 6],
    [7, 8, 9, 10],
];

console.log("Original matrix: ", matrix1);
console.log("New Matrix: ", markZeros(matrix1));
