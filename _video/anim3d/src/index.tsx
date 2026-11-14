import React from "react";
import { Composition, registerRoot } from "remotion";
import { PhoDemo, PHO_FRAMES } from "./videos/pho/Pho";
import { VangVideo, VANG_FRAMES } from "./videos/vang/Vang";
import { Bia } from "./videos/vang/Bia";
import { DatVideo, DAT_FRAMES } from "./videos/dat/Dat";
import { BiaDat } from "./videos/dat/BiaDat";
import { HnVideo, HN_FRAMES } from "./videos/hn/Hn";
import { LuongVideo, LUONG_FRAMES } from "./videos/luong/Luong";
const Root: React.FC = () => <>
  <Composition id="PhoDemo" component={PhoDemo} durationInFrames={PHO_FRAMES} fps={30} width={1920} height={1080} />
  <Composition id="Vang" component={VangVideo} durationInFrames={VANG_FRAMES} fps={30} width={1920} height={1080} />
  <Composition id="Dat" component={DatVideo} durationInFrames={DAT_FRAMES} fps={30} width={1920} height={1080} />
  <Composition id="Hn" component={HnVideo} durationInFrames={HN_FRAMES} fps={30} width={1920} height={1080} />
  <Composition id="Luong" component={LuongVideo} durationInFrames={LUONG_FRAMES} fps={30} width={1920} height={1080} />
  <Composition id="BiaDat" component={BiaDat} durationInFrames={1} fps={30} width={1920} height={1080} />
  <Composition id="Bia" component={Bia} durationInFrames={1} fps={30} width={1920} height={1080} />
</>;
registerRoot(Root);
