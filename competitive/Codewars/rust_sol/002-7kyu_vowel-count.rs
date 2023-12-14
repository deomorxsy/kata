fn get_count(string: &str) -> usize {
    let mut vowels_count: usize = 0;
    let vowels = vec!['a','e', 'i', 'o', 'u'];
    for i in string.chars() {
        if vowels.contains(&i) {
            vowels_count += 1;
        } else {
            ();
        }
    }
    return vowels_count;
}

