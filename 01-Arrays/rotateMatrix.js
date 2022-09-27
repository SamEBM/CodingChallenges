// Given an image represented by a NxN matrix of pixels, write a method to rotate the image 90 degrees clockwise and in place
// Time Complexity: O(n^2)
// The best time complexity since in every algorithm you need to "touch" every pixel once.

function rotate(matrix){

    if(matrix.length == 0 || matrix.length != matrix[0].length) return false;

    const n = matrix.length;
    for (let layer = 0; layer < n/2; layer++) {
        const first = layer;
        const last = n - 1 - layer;
        for (let i = first; i <last; i++) {
            const offset = i - first;

            // Save top
            const top = matrix[first][i];

            // Left edge -> top
            matrix[first][i] = matrix[last - offset][first];

            // Bottom edge -> left
            matrix[last - offset][first] = matrix[last][last - offset];

            // Right edge -> bottom
            matrix[last][last - offset] = matrix[i][last];

            // Top edge -> right
            matrix[i][last] = top;
        }
    }
    return matrix;
}

const matrix = [
    [1, 2, 3, 4, 5],
    [6, 7, 8, 9, 10],
    [11, 12, 13, 14, 15],
    [16, 17, 18, 19, 20],
    [21, 22, 23, 24, 25],
];

console.log("Original matrix: ", matrix);
console.log("Rotated 90 degrees: ", rotate(matrix))