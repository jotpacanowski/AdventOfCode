use std::collections::HashSet;
use std::fs;

const DAY: i32 = 3;
const FN: &str = "in3.txt";

fn main() {
    println!("Advent of Code day {:02}!", DAY);

    let input = fs::read_to_string(FN).expect("failed to read input file");
    let lines: Vec<&str> = input.lines().collect();

    println!("Read {} lines.", lines.len());
    println!("part1: {}", solve1(&lines));
    println!("part2: {}", solve2(&lines));
}

fn priority(letter: &char) -> u32 {
    let letter = *letter;
    if 'a' <= letter && letter <= 'z' {
        1 + letter as u32 - 'a' as u32
    } else if 'A' <= letter && letter <= 'Z' {
        27 + letter as u32 - 'A' as u32
    } else {
        panic!("bad letter")
    }
}

fn solve1(lines: &[&str]) -> u32 {
    let mut total = 0u32;

    fn single_line_common(line: &str) -> HashSet<char> {
        assert_eq!(line.len() % 2, 0);
        let a = &line[0..line.len() / 2];
        let b = &line[line.len() / 2..];
        assert_eq!(a.len(), b.len());

        let a: HashSet<char> = HashSet::from_iter(a.chars());
        let b: HashSet<char> = HashSet::from_iter(b.chars());

        a.intersection(&b)
            // .map(|x| *x)  // &char to char
            // .cloned()
            .copied()
            .collect()
    }

    for line in lines {
        total += single_line_common(line).iter().map(priority).sum::<u32>();
    }

    total
}

fn solve2(lines: &[&str]) -> u32 {
    let mut total = 0u32;

    let line_as_set = |idx: usize| HashSet::from_iter(lines[idx].chars());

    for i in (0..lines.len() - 2).step_by(3) {
        let a = line_as_set(i);
        let b = line_as_set(i + 1);
        let c = line_as_set(i + 2);

        // using .intersection() here got complicated quickly
        let p: HashSet<char> = &(&a & &b) & &c;
        let p: u32 = p.iter().map(priority).sum();
        total += p;
    }

    total
}
