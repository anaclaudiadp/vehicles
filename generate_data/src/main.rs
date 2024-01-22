extern crate chrono;
extern crate rand;
use chrono::prelude::DateTime;
use chrono::Utc;
use std::time::{UNIX_EPOCH, Duration};
use indexmap::IndexMap;
use rand::{Rng, SeedableRng};
use rand_chacha::ChaCha8Rng;
use rand::distributions::{Alphanumeric, DistString};
use std::fs::File;
use std::io::Write;
use clap::Parser;


#[derive(Parser)]
struct Cli {
    /// Random number seed
    seed: u64,

    /// Number of cars
    #[arg(short, long, default_value_t = 10)]
    cars: u64,

    /// Number of hours
    #[arg(long, default_value_t = 24)]
    hours: u64
}

fn main() {
    let args = Cli::parse();

    const TIME_INCREMENT_SECONDS: u64 = 60;  // 1 minute

    let mut rng = ChaCha8Rng::seed_from_u64(args.seed);

    let first_time = 1695885322;
    let last_time = first_time + (args.hours * 60 * 60);

    let mut cars = IndexMap::new();

    for _car_number in 1..=args.cars
    {
        let car_label = Alphanumeric.sample_string(&mut rng, 5);
        cars.insert(car_label.clone(), first_time);
    }

    let mut samples = File::create("samples.txt").expect("Failed to create file");

    while cars.len()>0 {
        let car_number = rng.gen_range(0..cars.len());
        let car_entry = cars.get_index(car_number).expect("Car should exist");
        let distance = rng.gen_range(1..100);
        let car_time = cars[car_entry.0];
        let car_label = car_entry.0.to_owned();
        cars.insert_full(car_label.clone(), car_time+TIME_INCREMENT_SECONDS);

        let datetime = DateTime::<Utc>::from(UNIX_EPOCH + Duration::from_secs(car_time));
        let timestamp_str = datetime.format("%Y-%m-%d %H:%M:%S").to_string();
        let data = format!("{},{},{}\n", timestamp_str, car_label, distance);
        samples.write_all(data.as_bytes()).expect("Failed to write");

        if car_time+TIME_INCREMENT_SECONDS >= last_time
        {
            cars.remove(&car_label);
        }
    }
}
