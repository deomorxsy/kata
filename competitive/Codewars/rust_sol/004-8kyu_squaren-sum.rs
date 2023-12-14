fn square_sum(vec: Vec<i32>) -> i32 {
    let mut squared = 0;
    for x in vec {
        squared = squared + x.pow(2);
    }
    return squared;
}
