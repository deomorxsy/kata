fn bool_to_word(value: bool) -> &'static str {
    if value == true {
        return "Yes"
    } else {
        return "No"
    }
}
