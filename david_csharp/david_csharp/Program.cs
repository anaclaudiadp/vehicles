
using System.Diagnostics;

var sw = new Stopwatch();
sw.Start();
var samples = File.ReadAllLines("/Users/davidbetteridge/Personal/vehicles/generate_data/target/debug/samples.txt");
sw.Stop();

Console.WriteLine("Read {0} samples in {1}s", samples.Length, sw.Elapsed.TotalSeconds);


// 2023-09-30 19:07:22,Yr2TN,24

// Total distance by vehicle
sw.Reset();
sw.Start();
var totalDistance = new Dictionary<string, double>();
foreach (var sample in samples)
{
    var bits = sample.Split(',');
    if (!totalDistance.ContainsKey(bits[1]))
        totalDistance.Add(bits[1], 0);
    
    // Skip out of range
    
    totalDistance[bits[1]] += double.Parse(bits[2]);
}

foreach (var kv in totalDistance)
{
    Console.WriteLine($"{kv.Key} travelled {kv.Value}");
}
sw.Stop();

Console.WriteLine("Summed samples in {0}s.", sw.Elapsed.TotalSeconds);


// Greatest distance travelled in 5 minutes
sw.Reset();
sw.Start();
var totalDistanceTravelled = new Dictionary<string, double>();
var totalDistanceWindow = new Dictionary<string, Queue<double>>();
foreach (var sample in samples)
{
    var bits = sample.Split(',');
    var carName = bits[1];
    if (!totalDistanceWindow.ContainsKey(carName))
    {
        totalDistanceWindow.Add(carName, new Queue<double>());
        totalDistanceTravelled.Add(carName, 0);
    }

    if (totalDistanceWindow[carName].Count >= 5)
        totalDistanceTravelled[carName] -= totalDistanceWindow[carName].Dequeue();

    totalDistanceTravelled[carName] += double.Parse(bits[2]);
    totalDistanceWindow[carName].Enqueue(double.Parse(bits[2]));
}
foreach (var kv in totalDistanceTravelled)
{
    Console.WriteLine($"{kv.Key} travelled {kv.Value} in 5 minutes");
}
sw.Stop();

Console.WriteLine("Windowed samples in {0}s.", sw.Elapsed.TotalSeconds);


// How many times did Car X over take Car Y?


// Repeat exersie with two seeds
