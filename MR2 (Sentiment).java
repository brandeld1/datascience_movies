import java.io.IOException;
import java.util.StringTokenizer;

import org.apache.hadoop.conf.Configuration;
import org.apache.hadoop.fs.Path;
import org.apache.hadoop.io.DoubleWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Job;
import org.apache.hadoop.mapreduce.Mapper;
import org.apache.hadoop.mapreduce.Reducer;
import org.apache.hadoop.mapreduce.lib.input.FileInputFormat;
import org.apache.hadoop.mapreduce.lib.output.FileOutputFormat;

public class test {

  public static class TokenizerMapper
       extends Mapper<Object, Text, Text, DoubleWritable>{

    private Text word = new Text();

    public void map(Object key, Text value, Context context
                    ) throws IOException, InterruptedException {
      StringTokenizer itr = new StringTokenizer(value.toString());
      itr.nextToken();
      while(itr.hasMoreTokens()) {
	    	  String data[] = itr.nextToken().toString().split(",");
	    	  if(data.length>=5) { //make sure the data is of correct size
		          String genresList = data[2]; //get the list of genres from the current line
		          String[] genres = genresList.toString().split("\\|"); //split the list of genres into an array
		          DoubleWritable sentiment = new DoubleWritable(Double.parseDouble(data[4])); //get the sentiment of the current line
		          for(int i=0;i<genres.length;i++){
		        	  String yeargenre = data[1]+","+genres[i]; //get the year and genre for each in the list
		        	  word.set(yeargenre); //set word as year,genre
		        	  context.write(word, sentiment); //add year,genre sentiment to context
		          }
	    	  }
	    }
    }
  }

  public static class DoubleSumReducer
       extends Reducer<Text,DoubleWritable,Text,DoubleWritable> {
    private DoubleWritable result = new DoubleWritable();

    public void reduce(Text key, Iterable<DoubleWritable> values,
                       Context context
                       ) throws IOException, InterruptedException {
      double sum = 0;
      int total = 0;
      for (DoubleWritable val : values) {
        sum += val.get(); // get the current value of sentiment
        total += 1; //get the total number of occurences
      }
      result.set(sum/total); //get the average
      context.write(key, result); //write the key,average 
    }
  }

  public static void main(String[] args) throws Exception {
    Configuration conf = new Configuration();
    Job job = Job.getInstance(conf, "word count");
    job.setJarByClass(test.class);
    job.setMapperClass(TokenizerMapper.class);
    job.setCombinerClass(DoubleSumReducer.class);
    job.setReducerClass(DoubleSumReducer.class);
    job.setOutputKeyClass(Text.class);
    job.setOutputValueClass(DoubleWritable.class);
    FileInputFormat.addInputPath(job, new Path(args[0]));
    FileOutputFormat.setOutputPath(job, new Path(args[1]));
    System.exit(job.waitForCompletion(true) ? 0 : 1);
  }
}