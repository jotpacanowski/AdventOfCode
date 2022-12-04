use std::fs;

fn main() {
    let lines = fs::read_to_string("in4.txt").expect("failed to read input file");
    let input = lines.lines().map(parse_line).collect::<Vec<_>>();

    println!("part1: {}", solve1(&input));
    println!("part2: {}", solve2(&input));
}

fn parse_line(line: &str) -> [i32; 4] {
    let l;
    let r;
    if let Some((lp, rp)) = line.split_once(',') {
        l = lp;
        r = rp;
    } else {
        panic!("bad line");
    }

    fn parse_range(ab: &str) -> [i32; 2] {
        if !ab.contains('-') {
            return [-1, -1];
        }
        if let Some((lp, rp)) = ab.split_once('-') {
            let l = lp.parse::<i32>();
            let p = rp.parse::<i32>();
            if l.is_err() || p.is_err() {
                panic!("int parse");
            }
            [l.unwrap(), p.unwrap()]
        } else {
            [-1, -1]
        }
    }

    parse_range(l)
        .iter()
        .chain(&parse_range(r))
        .copied()
        .collect::<Vec<_>>()
        .try_into()
        .unwrap()
}

fn solve1(input: &[[i32; 4]]) -> u32 {
    let mut total = 0u32;
    for [a, b, c, d] in input {
        let mut f = (a..=b).contains(&c) && (a..=b).contains(&d);
        f = f || ((c..=d).contains(&a) && (c..=d).contains(&b));
        if f {
            total += 1;
        }
    }
    total
}

fn solve2(inp: &[[i32; 4]]) -> u32 {
    inp.iter()
        .map(|[a, b, c, d]| if b < c || d < a { 0 } else { 1 })
        .sum()
}
