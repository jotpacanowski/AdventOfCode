use std::collections::HashSet;
use std::fs;

const DAY: i32 = 2;
const FN: &str = "in2.txt";

// const WINNING

fn parse_input(lines: Vec<&str>) -> Vec<(u8, u8)> {
    let mut r = Vec::with_capacity(lines.len());
    for line in lines {
        let l = line.split_ascii_whitespace();
        let l: Vec<&str> = l.collect();

        assert_eq!(l.len(), 2);
        debug_assert_eq!(l[0].len(), 1);
        debug_assert_eq!(l[1].len(), 1);

        let abc = l[0].chars().next().expect("wtf");
        let xyz = l[1].chars().next().expect("wtf2");
        r.push((abc as u8 - b'A', xyz as u8 - b'X'));
    }

    r
}

fn solve1(inp: &Vec<(u8, u8)>) -> u32 {
    let mut total = 0u32;

    let winning = HashSet::<(u8, u8)>::from(
        //
        [(0, 1), (1, 2), (2, 0)],
    );

    for (i, m) in inp {
        let i = *i as u32;
        let m = *m as u32;
        if i == m {
            total += 3 + (m + 1);
        } else if winning.get(&(i as u8, m as u8)).is_some() {
            total += 6 + (m + 1);
        } else {
            total += m + 1;
        }
    }

    total
}

fn solve2(inp: &Vec<(u8, u8)>) -> u32 {
    let mut total = 0u32;

    for (i, t) in inp {
        let i = *i as i8;
        total += match *t {
            0 => {
                // lose
                let m = (3 + i - 1) % 3;
                m + 1
            }
            1 => {
                // draw
                3 + (i + 1)
            }
            2 => {
                // win
                let m = (i + 1) % 3;
                6 + m + 1
            }
            _ => panic!("bad number"),
        } as u32;
    }

    total
}

fn main() {
    println!("Advent of Code day {:02}!", DAY);

    let input = fs::read_to_string(FN).expect("failed to read input file");
    let lines: Vec<&str> = input.lines().collect();

    println!("Read {} lines.", lines.len());

    let input = parse_input(lines);

    let part1 = solve1(&input);
    let part2 = solve2(&input);
    println!("part1: {}", part1);
    println!("part2: {}", part2);
}
