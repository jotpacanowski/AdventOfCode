use std::fs;

const DAY: i32 = 1;
const FN: &str = "in1.txt";

fn parse_input(lines: Vec<&str>) -> Vec<Vec<i32>> {
    let mut r: Vec<Vec<i32>> = Vec::with_capacity(20);
    let mut st: Vec<i32> = vec![];

    for l in lines {
        if let Ok(i) = l.parse::<i32>() {
            assert!(i > 0);
            st.push(i);
        } else {
            r.push(st);
            st = vec![];
        }
    }

    r
}

fn solve1(elves: &[Vec<i32>]) -> i32 {
    elves.iter().map(|x| x.iter().sum()).max().unwrap()
}

fn solve1_simple(elves: &[Vec<i32>]) -> i32 {
    let mut max = 0;
    for it in elves {
        let s = it.iter().sum();
        if s > max {
            max = s;
        }
    }
    max
}

fn solve2(elves: &[Vec<i32>]) -> i32 {
    let mut sums: Vec<i32> = elves.iter().map(|x| x.iter().sum()).collect();

    // sums.sort();
    sums.sort_unstable_by(|a, b| b.cmp(a));
    // eprintln!("DBG: {sums:?}");
    eprintln!("{:?}", &sums[..3]);

    sums[..3].iter().sum()
}

fn main() {
    println!("Advent of Code day {:02}!", DAY);

    let input = fs::read_to_string(FN).expect("failed to read input file");
    let lines: Vec<&str> = input.lines().collect();

    println!("Read {} lines.", lines.len());

    let elves = parse_input(lines);
    println!("-> {} elves", elves.len());

    println!("part1: {}", solve1(&elves));
    println!("part1: {}", solve1_simple(&elves));
    println!("part2: {}", solve2(&elves));
}
